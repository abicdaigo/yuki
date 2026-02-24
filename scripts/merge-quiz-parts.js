#!/usr/bin/env node
/**
 * Merge quiz question parts into a single quiz-questions.json
 * Reads from data/parts/*.json and writes to data/quiz-questions.json
 */
const fs = require('fs');
const path = require('path');

const PARTS_DIR = path.join(__dirname, '..', 'data', 'parts');
const OUTPUT = path.join(__dirname, '..', 'data', 'quiz-questions.json');

const CATEGORIES = ['current', 'tourism', 'history', 'entertainment', 'manga', 'food'];
const LEVELS = ['beginner', 'intermediate', 'advanced'];

const merged = {};
let totalQ = 0;
let errors = [];

for (const cat of CATEGORIES) {
  const filePath = path.join(PARTS_DIR, cat + '.json');
  if (!fs.existsSync(filePath)) {
    errors.push(`Missing: ${cat}.json`);
    continue;
  }

  let data;
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    data = JSON.parse(raw);
  } catch (e) {
    errors.push(`JSON parse error in ${cat}.json: ${e.message}`);
    continue;
  }

  merged[cat] = {};
  for (const lv of LEVELS) {
    if (!data[lv] || !Array.isArray(data[lv])) {
      errors.push(`${cat}.json missing level: ${lv}`);
      merged[cat][lv] = [];
      continue;
    }
    merged[cat][lv] = data[lv];
    totalQ += data[lv].length;
    console.log(`  ${cat}/${lv}: ${data[lv].length} questions`);
  }
}

if (errors.length > 0) {
  console.error('\nErrors:');
  errors.forEach(e => console.error('  - ' + e));
}

const output = {
  _meta: {
    version: 2,
    lastUpdated: new Date().toISOString().split('T')[0],
    totalQuestions: totalQ
  },
  ...merged
};

const json = JSON.stringify(output, null, 2);
const sizeMB = (Buffer.byteLength(json, 'utf8') / (1024 * 1024)).toFixed(2);

fs.writeFileSync(OUTPUT, json, 'utf8');
console.log(`\nDone! Total: ${totalQ} questions. Size: ${sizeMB} MB`);
console.log(`Written to: ${OUTPUT}`);

if (totalQ < 1800) {
  console.warn(`\nWARNING: Expected 1800 questions but got ${totalQ}`);
}
