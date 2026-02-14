/* ========================================
   Firebase Configuration
   ======================================== */

/*
 * SETUP INSTRUCTIONS:
 * 1. Go to https://console.firebase.google.com
 * 2. Create a new project (e.g., "webb-jcc")
 * 3. Enable Realtime Database (in test mode for development)
 * 4. Go to Project Settings > General > Your apps > Web app
 * 5. Register your web app and copy the config values below
 * 6. Replace the placeholder values with your actual Firebase config
 *
 * DATABASE RULES (for production, set in Firebase Console > Realtime Database > Rules):
 * {
 *   "rules": {
 *     "activities": {
 *       ".read": true,
 *       ".write": true
 *     }
 *   }
 * }
 */

const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    databaseURL: "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Firebase state
let firebaseApp = null;
let database = null;
let firebaseReady = false;

// Check if Firebase config is set up
function isFirebaseConfigured() {
    return firebaseConfig.apiKey !== "YOUR_API_KEY";
}

// Initialize Firebase
function initFirebase() {
    if (!isFirebaseConfigured()) {
        console.log('Firebase not configured. Voting system will run in demo/local mode.');
        console.log('To enable real-time voting, set up Firebase and update firebase-config.js');
        return false;
    }

    try {
        // Load Firebase SDK dynamically
        const script1 = document.createElement('script');
        script1.src = 'https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js';
        script1.onload = () => {
            const script2 = document.createElement('script');
            script2.src = 'https://www.gstatic.com/firebasejs/9.23.0/firebase-database-compat.js';
            script2.onload = () => {
                firebaseApp = firebase.initializeApp(firebaseConfig);
                database = firebase.database();
                firebaseReady = true;
                console.log('Firebase initialized successfully!');
                // Trigger voting system to load from Firebase
                if (typeof loadActivitiesFromFirebase === 'function') {
                    loadActivitiesFromFirebase();
                }
            };
            document.head.appendChild(script2);
        };
        document.head.appendChild(script1);
        return true;
    } catch (error) {
        console.error('Firebase initialization error:', error);
        return false;
    }
}

// Initialize on load
initFirebase();