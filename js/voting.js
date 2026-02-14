/* ========================================
   Voting System — Member Voting Display
   Admin management is handled in admin.html
   ======================================== */

// Browser fingerprint for preventing duplicate votes
function getBrowserFingerprint() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    ctx.textBaseline = 'top';
    ctx.font = '14px Arial';
    ctx.fillText('fingerprint', 2, 2);
    const canvasData = canvas.toDataURL();

    const data = [
        navigator.userAgent,
        navigator.language,
        screen.width + 'x' + screen.height,
        new Date().getTimezoneOffset(),
        canvasData.slice(-50)
    ].join('|');

    // Simple hash
    let hash = 0;
    for (let i = 0; i < data.length; i++) {
        const char = data.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }
    return 'user_' + Math.abs(hash).toString(36);
}

const VOTER_ID = getBrowserFingerprint();

// Local storage for demo mode (when Firebase not configured)
const LOCAL_STORAGE_KEY = 'jcc-activities';

function getLocalActivities() {
    try {
        return JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY)) || {};
    } catch {
        return {};
    }
}

function saveLocalActivities(activities) {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(activities));
}

/* --- Init --- */
document.addEventListener('DOMContentLoaded', () => {
    loadActivities();
});

function loadActivities() {
    if (firebaseReady) {
        loadActivitiesFromFirebase();
    } else {
        renderActivities();
    }
}

function loadActivitiesFromFirebase() {
    if (!firebaseReady) return;

    database.ref('activities').on('value', (snapshot) => {
        const data = snapshot.val() || {};
        saveLocalActivities(data);
        renderActivities();
    });
}

function renderActivities() {
    const container = document.getElementById('votingContainer');
    const emptyMsg = document.getElementById('votingEmpty');
    const activities = getLocalActivities();
    const activityIds = Object.keys(activities).sort((a, b) => {
        return (activities[b].createdAt || 0) - (activities[a].createdAt || 0);
    });

    // Clear existing cards (keep empty message)
    container.querySelectorAll('.voting-card').forEach(el => el.remove());

    if (activityIds.length === 0) {
        emptyMsg.classList.remove('hidden');
        return;
    }

    emptyMsg.classList.add('hidden');

    activityIds.forEach(id => {
        const activity = activities[id];
        const card = createVotingCard(id, activity);
        container.appendChild(card);
    });
}

function createVotingCard(id, activity) {
    const card = document.createElement('div');
    card.className = 'voting-card fade-in visible';

    const forCount = activity.votesFor ? Object.keys(activity.votesFor).length : 0;
    const againstCount = activity.votesAgainst ? Object.keys(activity.votesAgainst).length : 0;
    const totalVotes = forCount + againstCount;
    const forPercent = totalVotes > 0 ? (forCount / totalVotes * 100) : 50;
    const againstPercent = totalVotes > 0 ? (againstCount / totalVotes * 100) : 50;

    const hasVotedFor = activity.votesFor && activity.votesFor[VOTER_ID];
    const hasVotedAgainst = activity.votesAgainst && activity.votesAgainst[VOTER_ID];
    const hasVoted = hasVotedFor || hasVotedAgainst;
    const isOpen = activity.status === 'open';

    const statusClass = isOpen ? 'status-open' : 'status-closed';
    const statusText = isOpen ? getTranslation('statusOpen') : getTranslation('statusClosed');

    card.innerHTML = `
        <span class="voting-status ${statusClass}">${statusText}</span>
        <h4>${escapeHtml(activity.title)}</h4>
        <div class="voting-date">📅 ${activity.date || ''}</div>
        ${activity.description ? `<div class="voting-desc">${escapeHtml(activity.description)}</div>` : ''}

        <div class="vote-buttons">
            <button class="vote-btn vote-for ${hasVotedFor ? 'voted' : ''}"
                    ${hasVoted || !isOpen ? 'disabled' : ''}
                    onclick="vote('${id}', 'for')">
                ${getTranslation('voteFor')} (${forCount})
            </button>
            <button class="vote-btn vote-against ${hasVotedAgainst ? 'voted' : ''}"
                    ${hasVoted || !isOpen ? 'disabled' : ''}
                    onclick="vote('${id}', 'against')">
                ${getTranslation('voteAgainst')} (${againstCount})
            </button>
        </div>

        <div class="vote-progress">
            <div class="progress-bar">
                <div class="progress-for" style="width: ${totalVotes > 0 ? forPercent : 50}%">
                    ${totalVotes > 0 && forPercent >= 15 ? forCount : ''}
                </div>
                <div class="progress-against" style="width: ${totalVotes > 0 ? againstPercent : 50}%">
                    ${totalVotes > 0 && againstPercent >= 15 ? againstCount : ''}
                </div>
            </div>
            <div class="vote-count">
                <span>${getTranslation('votesFor')}: ${forCount}</span>
                <span>${getTranslation('votesAgainst')}: ${againstCount}</span>
            </div>
        </div>
    `;

    return card;
}

function vote(activityId, type) {
    const activities = getLocalActivities();
    const activity = activities[activityId];

    if (!activity || activity.status !== 'open') return;

    // Check if already voted
    if ((activity.votesFor && activity.votesFor[VOTER_ID]) ||
        (activity.votesAgainst && activity.votesAgainst[VOTER_ID])) {
        return;
    }

    if (type === 'for') {
        if (!activity.votesFor) activity.votesFor = {};
        activity.votesFor[VOTER_ID] = true;
    } else {
        if (!activity.votesAgainst) activity.votesAgainst = {};
        activity.votesAgainst[VOTER_ID] = true;
    }

    if (firebaseReady) {
        const path = type === 'for' ? 'votesFor' : 'votesAgainst';
        database.ref(`activities/${activityId}/${path}/${VOTER_ID}`).set(true);
    } else {
        saveLocalActivities(activities);
        renderActivities();
    }
}

// Utility: escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}