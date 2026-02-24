# -*- coding: utf-8 -*-
import json
import sys

# We'll build the full 100-question array
# First read what we have (questions 1-10)
with open(r"C:\Users\daigo\source\yuki\data\parts\history_advanced.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# Now add questions 11 through 100
new_questions = []

new_questions.append({
  "id": "history_advanced_011",
  "q": {
    "en": "What was the first of the six national histories (Rikkokushi) compiled during the Nara and Heian periods?",
    "zh": "\u5948\u826f\u548c\u5e73\u5b89\u65f6\u4ee3\u7f16\u7e82\u7684\u516d\u90e8\u56fd\u53f2\uff08\u516d\u56fd\u53f2\uff09\u4e2d\uff0c\u6700\u65e9\u7684\u4e00\u90e8\u662f\u4ec0\u4e48\uff1f",
    "ja": "\u5948\u826f\u30fb\u5e73\u5b89\u6642\u4ee3\u306b\u7de8\u7e82\u3055\u308c\u305f\u516d\u56fd\u53f2\u306e\u3046\u3061\u3001\u6700\u521d\u306e\u3082\u306e\u306f\u4f55\u3067\u3059\u304b\uff1f",
    "es": "\u00bfCu\u00e1l fue la primera de las seis historias nacionales (Rikkokushi) compiladas durante los per\u00edodos Nara y Heian?"
  },
  "c": [
    {"en": "Shoku Nihongi", "zh": "\u7eed\u65e5\u672c\u7eaa", "ja": "\u7d9a\u65e5\u672c\u7d00", "es": "Shoku Nihongi"},
    {"en": "Nihon Shoki (Nihongi)", "zh": "\u65e5\u672c\u4e66\u7eaa", "ja": "\u65e5\u672c\u66f8\u7d00", "es": "Nihon Shoki (Nihongi)"},
    {"en": "Kojiki", "zh": "\u53e4\u4e8b\u8bb0", "ja": "\u53e4\u4e8b\u8a18", "es": "Kojiki"},
    {"en": "Nihon Sandai Jitsuroku", "zh": "\u65e5\u672c\u4e09\u4ee3\u5b9e\u5f55", "ja": "\u65e5\u672c\u4e09\u4ee3\u5b9f\u9332", "es": "Nihon Sandai Jitsuroku"}
  ],
  "a": 1,
  "trivia": {
    "en": "The Nihon Shoki (720 CE) is the first of the six national histories and the oldest official chronicle of Japan, written in classical Chinese.",
    "zh": "\u300a\u65e5\u672c\u4e66\u7eaa\u300b\uff08720\u5e74\uff09\u662f\u516d\u56fd\u53f2\u4e4b\u9996\uff0c\u4e5f\u662f\u65e5\u672c\u6700\u53e4\u8001\u7684\u5b98\u65b9\u7f16\u5e74\u53f2\uff0c\u4ee5\u6c49\u6587\u5199\u6210\u3002",
    "ja": "\u300e\u65e5\u672c\u66f8\u7d00\u300f\uff08720\u5e74\uff09\u306f\u516d\u56fd\u53f2\u306e\u6700\u521d\u3067\u3042\u308a\u3001\u6f22\u6587\u3067\u66f8\u304b\u308c\u305f\u65e5\u672c\u6700\u53e4\u306e\u6b63\u53f2\u3067\u3059\u3002",
    "es": "El Nihon Shoki (720 d.C.) es la primera de las seis historias nacionales y la cr\u00f3nica oficial m\u00e1s antigua de Jap\u00f3n, escrita en chino cl\u00e1sico."
  }
})

new_questions.append({
  "id": "history_advanced_012",
  "q": {
    "en": "Emperor Shomu's establishment of Todai-ji and its Great Buddha in Nara was influenced by which Buddhist school?",
    "zh": "\u5723\u6b66\u5929\u7687\u5728\u5948\u826f\u5efa\u7acb\u4e1c\u5927\u5bfa\u53ca\u5176\u5927\u4f5b\u53d7\u5230\u4e86\u54ea\u4e2a\u4f5b\u6559\u5b97\u6d3e\u7684\u5f71\u54cd\uff1f",
    "ja": "\u8056\u6b66\u5929\u7687\u304c\u5948\u826f\u306b\u6771\u5927\u5bfa\u3068\u5927\u4ecf\u3092\u5efa\u7acb\u3057\u305f\u306e\u306f\u3001\u3069\u306e\u4ecf\u6559\u601d\u60f3\u306e\u5f71\u97ff\u3067\u3059\u304b\uff1f",
    "es": "\u00bfQu\u00e9 escuela budista influy\u00f3 en la construcci\u00f3n del templo Todai-ji y su Gran Buda en Nara por el Emperador Shomu?"
  },
  "c": [
    {"en": "Pure Land Buddhism (Jodo)", "zh": "\u51c0\u571f\u5b97", "ja": "\u6d44\u571f\u6559", "es": "Budismo de la Tierra Pura (Jodo)"},
    {"en": "Zen Buddhism", "zh": "\u7985\u5b97", "ja": "\u7985\u5b97", "es": "Budismo Zen"},
    {"en": "Kegon (Huayan) Buddhism", "zh": "\u534e\u4e25\u5b97", "ja": "\u83ef\u53b3\u5b97", "es": "Budismo Kegon (Huayan)"},
    {"en": "Nichiren Buddhism", "zh": "\u65e5\u83b2\u5b97", "ja": "\u65e5\u84ee\u5b97", "es": "Budismo Nichiren"}
  ],
  "a": 2,
  "trivia": {
    "en": "The Daibutsu represents Vairocana Buddha, and Todai-ji served as the head temple of the provincial temple system (kokubunji) established by Shomu.",
    "zh": "\u5927\u4f5b\u4ee3\u8868\u6bd7\u5362\u906e\u90a3\u4f5b\uff0c\u4e1c\u5927\u5bfa\u662f\u5723\u6b66\u5929\u7687\u8bbe\u7acb\u7684\u56fd\u5206\u5bfa\u5236\u5ea6\u7684\u603b\u5bfa\u3002",
    "ja": "\u5927\u4ecf\u306f\u6bd8\u76e7\u906e\u90a3\u4ecf\u3092\u8868\u3057\u3001\u6771\u5927\u5bfa\u306f\u8056\u6b66\u5929\u7687\u304c\u8a2d\u7acb\u3057\u305f\u56fd\u5206\u5bfa\u5236\u5ea6\u306e\u7dcf\u672c\u5c71\u3067\u3057\u305f\u3002",
    "es": "El Daibutsu representa al Buda Vairocana, y Todai-ji sirvi\u00f3 como templo principal del sistema de templos provinciales (kokubunji) establecido por Shomu."
  }
})

new_questions.append({
  "id": "history_advanced_013",
  "q": {
    "en": "What artificial island in Nagasaki harbor served as the sole point of European trade during Japan's sakoku period?",
    "zh": "\u5728\u65e5\u672c\u9501\u56fd\u65f6\u671f\uff0c\u957f\u5d0e\u6e2f\u7684\u54ea\u4e2a\u4eba\u5de5\u5c9b\u662f\u6b27\u6d32\u8d38\u6613\u7684\u552f\u4e00\u636e\u70b9\uff1f",
    "ja": "\u9396\u56fd\u6642\u4ee3\u3001\u9577\u5d0e\u6e2f\u306e\u3069\u306e\u4eba\u5de5\u5cf6\u304c\u30e8\u30fc\u30ed\u30c3\u30d1\u3068\u306e\u552f\u4e00\u306e\u8cbf\u6613\u62e0\u70b9\u3067\u3057\u305f\u304b\uff1f",
    "es": "\u00bfQu\u00e9 isla artificial en el puerto de Nagasaki sirvi\u00f3 como \u00fanico punto de comercio europeo durante el per\u00edodo sakoku de Jap\u00f3n?"
  },
  "c": [
    {"en": "Hashima Island", "zh": "\u7aef\u5c9b", "ja": "\u7aef\u5cf6", "es": "Isla Hashima"},
    {"en": "Hirado Island", "zh": "\u5e73\u6237\u5c9b", "ja": "\u5e73\u6238\u5cf6", "es": "Isla Hirado"},
    {"en": "Dejima", "zh": "\u51fa\u5c9b", "ja": "\u51fa\u5cf6", "es": "Dejima"},
    {"en": "Enoshima", "zh": "\u6c5f\u4e4b\u5c9b", "ja": "\u6c5f\u306e\u5cf6", "es": "Enoshima"}
  ],
  "a": 2,
  "trivia": {
    "en": "Dejima was originally built in 1636 for Portuguese traders; after their expulsion in 1639, the Dutch East India Company (VOC) was relocated there from Hirado in 1641.",
    "zh": "\u51fa\u5c9b\u6700\u521d\u4e8e1636\u5e74\u4e3a\u8461\u8404\u7259\u5546\u4eba\u5efa\u9020\uff1b1639\u5e74\u8461\u8404\u7259\u4eba\u88ab\u9a71\u9010\u540e\uff0c\u8377\u5170\u4e1c\u5370\u5ea6\u516c\u53f8\u4e8e1641\u5e74\u4ece\u5e73\u6237\u8fc1\u81f3\u6b64\u5904\u3002",
    "ja": "\u51fa\u5cf6\u306f1636\u5e74\u306b\u30dd\u30eb\u30c8\u30ac\u30eb\u5546\u4eba\u306e\u305f\u3081\u306b\u5efa\u8a2d\u3055\u308c\u307e\u3057\u305f\u304c\u30011639\u5e74\u306e\u8ffd\u653e\u5f8c\u30011641\u5e74\u306b\u30aa\u30e9\u30f3\u30c0\u6771\u30a4\u30f3\u30c9\u4f1a\u793e\u304c\u5e73\u6238\u304b\u3089\u79fb\u3055\u308c\u307e\u3057\u305f\u3002",
    "es": "Dejima fue construida originalmente en 1636 para comerciantes portugueses; tras su expulsi\u00f3n en 1639, la Compa\u00f1\u00eda Holandesa de las Indias Orientales (VOC) fue reubicada all\u00ed desde Hirado en 1641."
  }
})

new_questions.append({
  "id": "history_advanced_014",
  "q": {
    "en": "The 'Osei Fukko no Daigourei' of January 3, 1868 was a proclamation that did what?",
    "zh": "1868\u5e741\u67083\u65e5\u7684\u201c\u738b\u653f\u590d\u53e4\u5927\u53f7\u4ee4\u201d\u662f\u4ec0\u4e48\uff1f",
    "ja": "\u6176\u5fdc3\u5e7412\u67089\u65e5\uff081868\u5e741\u67083\u65e5\uff09\u306e\u300c\u738b\u653f\u5fa9\u53e4\u306e\u5927\u53f7\u4ee4\u300d\u3068\u306f\u4f55\u3067\u3059\u304b\uff1f",
    "es": "\u00bfQu\u00e9 fue el 'Osei Fukko no Daigourei' del 3 de enero de 1868?"
  },
  "c": [
    {"en": "A declaration of war against the Western powers", "zh": "\u5bf9\u897f\u65b9\u5217\u5f3a\u7684\u5ba3\u6218", "ja": "\u897f\u6d0b\u5217\u5f37\u3078\u306e\u5ba3\u6226\u5e03\u544a", "es": "Una declaraci\u00f3n de guerra contra las potencias occidentales"},
    {"en": "A decree abolishing the samurai class", "zh": "\u5e9f\u9664\u6b66\u58eb\u9636\u7ea7\u7684\u6cd5\u4ee4", "ja": "\u6b66\u58eb\u968e\u7d1a\u3092\u5ec3\u6b62\u3059\u308b\u52c5\u4ee4", "es": "Un decreto que abol\u00eda la clase samur\u00e1i"},
    {"en": "A treaty opening all Japanese ports to foreign trade", "zh": "\u5411\u5916\u56fd\u8d38\u6613\u5f00\u653e\u6240\u6709\u65e5\u672c\u6e2f\u53e3\u7684\u6761\u7ea6", "ja": "\u5168\u3066\u306e\u65e5\u672c\u306e\u6e2f\u3092\u5916\u56fd\u8cbf\u6613\u306b\u958b\u653e\u3059\u308b\u6761\u7d04", "es": "Un tratado que abr\u00eda todos los puertos japoneses al comercio exterior"},
    {"en": "A proclamation abolishing the shogunate and restoring direct imperial rule", "zh": "\u5e9f\u9664\u5e55\u5e9c\u3001\u6062\u590d\u5929\u7687\u4eb2\u653f\u7684\u5ba3\u8a00", "ja": "\u5e55\u5e9c\u3092\u5ec3\u6b62\u3057\u5929\u7687\u89aa\u653f\u3092\u5fa9\u6d3b\u3055\u305b\u308b\u5ba3\u8a00", "es": "Una proclamaci\u00f3n que abol\u00eda el shogunato y restauraba el gobierno imperial directo"}
  ],
  "a": 3,
  "trivia": {
    "en": "The decree established the new government with three offices: President (Sosai), Senior Councillors (Gijo), and Junior Councillors (Sanyo).",
    "zh": "\u8be5\u53f7\u4ee4\u4ee5\u4e09\u804c\u5236\u5efa\u7acb\u4e86\u65b0\u653f\u5e9c\uff1a\u603b\u88c1\u3001\u8bae\u5b9a\u548c\u53c2\u4e0e\u3002",
    "ja": "\u3053\u306e\u5927\u53f7\u4ee4\u306b\u3088\u308a\u4e09\u8077\u5236\uff08\u7dcf\u88c1\u30fb\u8b70\u5b9a\u30fb\u53c2\u4e0e\uff09\u306e\u65b0\u653f\u5e9c\u304c\u6a39\u7acb\u3055\u308c\u307e\u3057\u305f\u3002",
    "es": "El decreto estableci\u00f3 el nuevo gobierno con tres cargos: Presidente (Sosai), Consejeros Superiores (Gijo) y Consejeros Menores (Sanyo)."
  }
})

new_questions.append({
  "id": "history_advanced_015",
  "q": {
    "en": "Who primarily carried out the assassination of Ii Naosuke in the Sakuradamon Incident (1860)?",
    "zh": "\u6a31\u7530\u95e8\u4e4b\u53d8\uff081860\u5e74\uff09\u4e2d\u6697\u6740\u4e95\u4f0a\u76f4\u5f3c\u7684\u4e3b\u8981\u662f\u54ea\u4e9b\u4eba\uff1f",
    "ja": "\u685c\u7530\u9580\u5916\u306e\u5909\uff081860\u5e74\uff09\u3067\u4e95\u4f0a\u76f4\u5f3c\u3092\u6697\u6bba\u3057\u305f\u306e\u306f\u4e3b\u306b\u8ab0\u3067\u3059\u304b\uff1f",
    "es": "\u00bfQui\u00e9nes llevaron a cabo principalmente el asesinato de Ii Naosuke en el Incidente de Sakuradamon (1860)?"
  },
  "c": [
    {"en": "Satsuma ronin acting alone", "zh": "\u5355\u72ec\u884c\u52a8\u7684\u8428\u6469\u6d6a\u4eba", "ja": "\u5358\u72ec\u884c\u52d5\u306e\u85a9\u6469\u6d6a\u58eb", "es": "Ronin de Satsuma actuando solo"},
    {"en": "Choshu loyalists", "zh": "\u957f\u5dde\u52e4\u738b\u5fd7\u58eb", "ja": "\u9577\u5dde\u306e\u5c0a\u738b\u5fd7\u58eb", "es": "Leales de Choshu"},
    {"en": "A group of Mito ronin (with one Satsuma samurai)", "zh": "\u4e00\u7fa4\u6c34\u6237\u6d6a\u4eba\uff08\u542b\u4e00\u540d\u8428\u6469\u6b66\u58eb\uff09", "ja": "\u6c34\u6238\u6d6a\u58eb\u306e\u4e00\u56e3\uff08\u85a9\u6469\u85e9\u58eb1\u540d\u3092\u542b\u3080\uff09", "es": "Un grupo de ronin de Mito (con un samur\u00e1i de Satsuma)"},
    {"en": "Tosa loyalist volunteers", "zh": "\u571f\u4f50\u52e4\u738b\u4e49\u52c7\u519b", "ja": "\u571f\u4f50\u306e\u52e4\u738b\u7fa9\u52c7\u8ecd", "es": "Voluntarios leales de Tosa"}
  ],
  "a": 2,
  "trivia": {
    "en": "Ii Naosuke was the Tairo who had signed the Harris Treaty without imperial approval and initiated the Ansei Purge against political opponents.",
    "zh": "\u4e95\u4f0a\u76f4\u5f3c\u662f\u5927\u8001\uff0c\u66fe\u672a\u7ecf\u5929\u7687\u6279\u51c6\u7b7e\u7f72\u4e86\u54c8\u91cc\u65af\u6761\u7ea6\uff0c\u5e76\u53d1\u52a8\u4e86\u5b89\u653f\u5927\u72f1\u3002",
    "ja": "\u4e95\u4f0a\u76f4\u5f3c\u306f\u5927\u8001\u3068\u3057\u3066\u52c5\u8a31\u306a\u304f\u65e5\u7c73\u4fee\u597d\u901a\u5546\u6761\u7d04\u306b\u8abf\u5370\u3057\u3001\u5b89\u653f\u306e\u5927\u7344\u3067\u653f\u6cbb\u7684\u53cd\u5bfe\u8005\u3092\u5f3e\u5727\u3057\u307e\u3057\u305f\u3002",
    "es": "Ii Naosuke era el Tairo que hab\u00eda firmado el Tratado Harris sin aprobaci\u00f3n imperial e inici\u00f3 la Purga Ansei contra los opositores pol\u00edticos."
  }
})

new_questions.append({
  "id": "history_advanced_016",
  "q": {
    "en": "Which SCAP directive ordered the dissolution of the zaibatsu holding companies during the Allied occupation?",
    "zh": "\u76df\u519b\u5360\u9886\u671f\u95f4\uff0c\u54ea\u9879SCAP\u6307\u4ee4\u4e0b\u4ee4\u89e3\u6563\u8d22\u9600\u63a7\u80a1\u516c\u53f8\uff1f",
    "ja": "\u9023\u5408\u56fd\u5360\u9818\u671f\u9593\u4e2d\u3001\u8ca1\u95a5\u6301\u682a\u4f1a\u793e\u306e\u89e3\u4f53\u3092\u547d\u3058\u305fSCAP\u6307\u4ee4\u306f\u4f55\u3067\u3059\u304b\uff1f",
    "es": "\u00bfQu\u00e9 directiva del SCAP orden\u00f3 la disoluci\u00f3n de las compa\u00f1\u00edas holding de los zaibatsu durante la ocupaci\u00f3n aliada?"
  },
  "c": [
    {"en": "The Dodge Line", "zh": "\u9053\u5947\u8def\u7ebf", "ja": "\u30c9\u30c3\u30b8\u30fb\u30e9\u30a4\u30f3", "es": "La L\u00ednea Dodge"},
    {"en": "SCAPIN-244 (Dissolution of Holding Companies)", "zh": "SCAPIN-244\uff08\u63a7\u80a1\u516c\u53f8\u89e3\u6563\u4ee4\uff09", "ja": "SCAPIN-244\uff08\u6301\u682a\u4f1a\u793e\u89e3\u4f53\u4ee4\uff09", "es": "SCAPIN-244 (Disoluci\u00f3n de Compa\u00f1\u00edas Holding)"},
    {"en": "The Reverse Course directive", "zh": "\u9006\u8f6c\u8def\u7ebf\u6307\u4ee4", "ja": "\u9006\u30b3\u30fc\u30b9\u6307\u4ee4", "es": "La directiva del Curso Inverso"},
    {"en": "SCAPIN-1000 (Economic Democratization Order)", "zh": "SCAPIN-1000\uff08\u7ecf\u6d4e\u6c11\u4e3b\u5316\u4ee4\uff09", "ja": "SCAPIN-1000\uff08\u7d4c\u6e08\u6c11\u4e3b\u5316\u4ee4\uff09", "es": "SCAPIN-1000 (Orden de Democratizaci\u00f3n Econ\u00f3mica)"}
  ],
  "a": 1,
  "trivia": {
    "en": "The four largest zaibatsu -- Mitsui, Mitsubishi, Sumitomo, and Yasuda -- were targeted first, though many reformed as keiretsu groups after the occupation.",
    "zh": "\u56db\u5927\u8d22\u9600\u2014\u2014\u4e09\u4e95\u3001\u4e09\u83f1\u3001\u4f4f\u53cb\u548c\u5b89\u7530\u2014\u2014\u9996\u5148\u88ab\u89e3\u6563\uff0c\u4f46\u8bb8\u591a\u5728\u5360\u9886\u7ed3\u675f\u540e\u4ee5\u7cfb\u5217\u96c6\u56e2\u7684\u5f62\u5f0f\u91cd\u7ec4\u3002",
    "ja": "\u4e09\u4e95\u30fb\u4e09\u83f1\u30fb\u4f4f\u53cb\u30fb\u5b89\u7530\u306e\u56db\u5927\u8ca1\u95a5\u304c\u6700\u521d\u306b\u5bfe\u8c61\u3068\u306a\u308a\u307e\u3057\u305f\u304c\u3001\u5360\u9818\u7d42\u4e86\u5f8c\u306b\u591a\u304f\u304c\u7cfb\u5217\u3068\u3057\u3066\u518d\u7de8\u3055\u308c\u307e\u3057\u305f\u3002",
    "es": "Los cuatro mayores zaibatsu -- Mitsui, Mitsubishi, Sumitomo y Yasuda -- fueron los primeros objetivos, aunque muchos se reformaron como grupos keiretsu despu\u00e9s de la ocupaci\u00f3n."
  }
})

new_questions.append({
  "id": "history_advanced_017",
  "q": {
    "en": "Which Heian-period practice involved retired emperors ruling from behind the scenes?",
    "zh": "\u5e73\u5b89\u65f6\u4ee3\u54ea\u79cd\u505a\u6cd5\u662f\u9000\u4f4d\u5929\u7687\u5728\u5e55\u540e\u6267\u653f\uff1f",
    "ja": "\u5e73\u5b89\u6642\u4ee3\u306b\u9000\u4f4d\u3057\u305f\u5929\u7687\u304c\u5b9f\u6a29\u3092\u63e1\u3063\u3066\u653f\u6cbb\u3092\u884c\u3046\u5236\u5ea6\u3092\u4f55\u3068\u8a00\u3044\u307e\u3059\u304b\uff1f",
    "es": "\u00bfQu\u00e9 pr\u00e1ctica del per\u00edodo Heian involucraba a emperadores retirados gobernando entre bastidores?"
  },
  "c": [
    {"en": "Insei (Cloistered rule)", "zh": "\u9662\u653f", "ja": "\u9662\u653f", "es": "Insei (Gobierno claustral)"},
    {"en": "Sekkan seiji (Regency government)", "zh": "\u6444\u5173\u653f\u6cbb", "ja": "\u6442\u95a2\u653f\u6cbb", "es": "Sekkan seiji (Gobierno de regencia)"},
    {"en": "Bakufu (Tent government)", "zh": "\u5e55\u5e9c", "ja": "\u5e55\u5e9c", "es": "Bakufu (Gobierno de tienda)"},
    {"en": "Mandokoro (Administrative board)", "zh": "\u653f\u6240", "ja": "\u653f\u6240", "es": "Mandokoro (Junta administrativa)"}
  ],
  "a": 0,
  "trivia": {
    "en": "Emperor Shirakawa initiated insei in 1086 and wielded enormous power as a retired emperor for over 40 years, controlling three successive emperors.",
    "zh": "\u767d\u6cb3\u5929\u7687\u4e8e1086\u5e74\u5f00\u521b\u9662\u653f\uff0c\u4f5c\u4e3a\u4e0a\u7687\u638c\u6743\u8d85\u8fc740\u5e74\uff0c\u63a7\u5236\u4e86\u4e09\u4ee3\u5929\u7687\u3002",
    "ja": "\u767d\u6cb3\u5929\u7687\u304c1086\u5e74\u306b\u9662\u653f\u3092\u958b\u59cb\u3057\u3001\u4e0a\u7687\u3068\u3057\u306640\u5e74\u4ee5\u4e0a\u306b\u308f\u305f\u308a\u7d76\u5927\u306a\u6a29\u529b\u3092\u632f\u308b\u3044\u30013\u4ee3\u306e\u5929\u7687\u3092\u652f\u914d\u3057\u307e\u3057\u305f\u3002",
    "es": "El Emperador Shirakawa inici\u00f3 el insei en 1086 y ejerci\u00f3 un enorme poder como emperador retirado durante m\u00e1s de 40 a\u00f1os, controlando a tres emperadores sucesivos."
  }
})

new_questions.append({
  "id": "history_advanced_018",
  "q": {
    "en": "What was the primary purpose of the Taika Reforms (645 CE)?",
    "zh": "\u5927\u5316\u6539\u65b0\uff08645\u5e74\uff09\u7684\u4e3b\u8981\u76ee\u7684\u662f\u4ec0\u4e48\uff1f",
    "ja": "\u5927\u5316\u306e\u6539\u65b0\uff08645\u5e74\uff09\u306e\u4e3b\u306a\u76ee\u7684\u306f\u4f55\u3067\u3057\u305f\u304b\uff1f",
    "es": "\u00bfCu\u00e1l fue el prop\u00f3sito principal de las Reformas Taika (645 d.C.)?"
  },
  "c": [
    {"en": "To establish Buddhism as the state religion", "zh": "\u5c06\u4f5b\u6559\u786e\u7acb\u4e3a\u56fd\u6559", "ja": "\u4ecf\u6559\u3092\u56fd\u6559\u3068\u3059\u308b\u3053\u3068", "es": "Establecer el budismo como religi\u00f3n estatal"},
    {"en": "To centralize government power under the Emperor by nationalizing land and reforming taxation", "zh": "\u901a\u8fc7\u571f\u5730\u56fd\u6709\u5316\u548c\u7a0e\u5236\u6539\u9769\u5c06\u653f\u6743\u96c6\u4e2d\u4e8e\u5929\u7687", "ja": "\u571f\u5730\u306e\u56fd\u6709\u5316\u3068\u7a0e\u5236\u6539\u9769\u306b\u3088\u308a\u5929\u7687\u306e\u3082\u3068\u306b\u653f\u6a29\u3092\u96c6\u4e2d\u3055\u305b\u308b\u3053\u3068", "es": "Centralizar el poder gubernamental bajo el Emperador mediante la nacionalizaci\u00f3n de tierras y la reforma fiscal"},
    {"en": "To open Japan to Chinese immigration", "zh": "\u5411\u4e2d\u56fd\u79fb\u6c11\u5f00\u653e\u65e5\u672c", "ja": "\u4e2d\u56fd\u304b\u3089\u306e\u79fb\u6c11\u3092\u53d7\u3051\u5165\u308c\u308b\u3053\u3068", "es": "Abrir Jap\u00f3n a la inmigraci\u00f3n china"},
    {"en": "To create a professional standing army", "zh": "\u5efa\u7acb\u4e00\u652f\u804c\u4e1a\u5e38\u5907\u519b", "ja": "\u8077\u696d\u7684\u306a\u5e38\u5099\u8ecd\u3092\u5275\u8a2d\u3059\u308b\u3053\u3068", "es": "Crear un ej\u00e9rcito profesional permanente"}
  ],
  "a": 1,
  "trivia": {
    "en": "The reforms were initiated after Prince Naka no Oe and Nakatomi no Kamatari overthrew the powerful Soga clan in the Isshi Incident.",
    "zh": "\u6539\u9769\u662f\u5728\u4e2d\u5927\u5144\u7687\u5b50\u548c\u4e2d\u81e3\u9550\u8db3\u5728\u4e59\u5df3\u4e4b\u53d8\u4e2d\u63a8\u7ffb\u82cf\u6211\u6c0f\u4e4b\u540e\u53d1\u8d77\u7684\u3002",
    "ja": "\u6539\u9769\u306f\u4e2d\u5927\u5144\u7687\u5b50\u3068\u4e2d\u81e3\u938c\u8db3\u304c\u4e59\u5df3\u306e\u5909\u3067\u8607\u6211\u6c0f\u3092\u5012\u3057\u305f\u5f8c\u306b\u958b\u59cb\u3055\u308c\u307e\u3057\u305f\u3002",
    "es": "Las reformas se iniciaron despu\u00e9s de que el Pr\u00edncipe Naka no Oe y Nakatomi no Kamatari derrocaron al poderoso clan Soga en el Incidente Isshi."
  }
})

new_questions.append({
  "id": "history_advanced_019",
  "q": {
    "en": "Which archaeological site in Saga Prefecture is the largest Yayoi-period settlement in Japan, featuring defensive moats?",
    "zh": "\u4f50\u8d3a\u53bf\u7684\u54ea\u4e2a\u8003\u53e4\u9057\u5740\u662f\u65e5\u672c\u6700\u5927\u7684\u5f25\u751f\u65f6\u4ee3\u805a\u843d\uff0c\u5177\u6709\u9632\u5fa1\u6027\u73af\u58d5\uff1f",
    "ja": "\u4f50\u8cc0\u770c\u306e\u3069\u306e\u907a\u8de1\u304c\u3001\u9632\u5fa1\u7684\u306a\u74b0\u6feb\u3092\u6301\u3064\u65e5\u672c\u6700\u5927\u7d1a\u306e\u5f25\u751f\u6642\u4ee3\u306e\u96c6\u843d\u8de1\u3067\u3059\u304b\uff1f",
    "es": "\u00bfQu\u00e9 sitio arqueol\u00f3gico en la Prefectura de Saga es el asentamiento m\u00e1s grande del per\u00edodo Yayoi en Jap\u00f3n, con fosos defensivos?"
  },
  "c": [
    {"en": "Yoshinogari", "zh": "\u5409\u91ce\u91cc", "ja": "\u5409\u91ce\u30f6\u91cc", "es": "Yoshinogari"},
    {"en": "Itazuke", "zh": "\u677f\u4ed8", "ja": "\u677f\u4ed8", "es": "Itazuke"},
    {"en": "Toro", "zh": "\u767b\u5442", "ja": "\u767b\u5442", "es": "Toro"},
    {"en": "Karako-Kagi", "zh": "\u5510\u53e4\u00b7\u952e", "ja": "\u5510\u53e4\u30fb\u9375", "es": "Karako-Kagi"}
  ],
  "a": 0,
  "trivia": {
    "en": "Yoshinogari features inner and outer moats, watchtowers, raised-floor storehouses, and burial jars, suggesting a proto-state society.",
    "zh": "\u5409\u91ce\u91cc\u6709\u5185\u5916\u73af\u58d5\u3001\u671b\u697c\u3001\u9ad8\u5e8a\u5f0f\u4ed3\u5e93\u548c\u74ee\u68fa\u5893\u846c\uff0c\u6697\u793a\u7740\u4e00\u4e2a\u539f\u59cb\u56fd\u5bb6\u793e\u4f1a\u3002",
    "ja": "\u5409\u91ce\u30f6\u91cc\u306b\u306f\u5185\u58d5\u30fb\u5916\u58d5\u3001\u7269\u898b\u6aed\u3001\u9ad8\u5e8a\u5f0f\u5009\u5eab\u3001\u7515\u68fa\u58b3\u306a\u3069\u304c\u3042\u308a\u3001\u521d\u671f\u56fd\u5bb6\u7684\u306a\u793e\u4f1a\u3092\u793a\u5506\u3057\u3066\u3044\u307e\u3059\u3002",
    "es": "Yoshinogari presenta fosos interiores y exteriores, atalayas, almacenes elevados y urnas funerarias, sugiriendo una sociedad proto-estatal."
  }
})

new_questions.append({
  "id": "history_advanced_020",
  "q": {
    "en": "What was the Ritsuryo system that governed Japan from the 7th to 10th centuries?",
    "zh": "\u5f8b\u4ee4\u5236\u5ea6\u662f\u4ec0\u4e48\uff0c\u5b83\u57287\u81f310\u4e16\u7eaa\u5982\u4f55\u6cbb\u7406\u65e5\u672c\uff1f",
    "ja": "7\u4e16\u7d00\u304b\u308910\u4e16\u7d00\u306b\u304b\u3051\u3066\u65e5\u672c\u3092\u7d71\u6cbb\u3057\u305f\u300c\u5f8b\u4ee4\u300d\u5236\u5ea6\u3068\u306f\u4f55\u3067\u3059\u304b\uff1f",
    "es": "\u00bfQu\u00e9 era el sistema Ritsuryo que gobern\u00f3 Jap\u00f3n del siglo VII al X?"
  },
  "c": [
    {"en": "A feudal system based on vassal-lord relationships", "zh": "\u57fa\u4e8e\u4e3b\u4ece\u5173\u7cfb\u7684\u5c01\u5efa\u5236\u5ea6", "ja": "\u4e3b\u5f93\u95a2\u4fc2\u306b\u57fa\u3065\u304f\u5c01\u5efa\u5236\u5ea6", "es": "Un sistema feudal basado en relaciones vasallo-se\u00f1or"},
    {"en": "A religious governance system led by Buddhist monks", "zh": "\u7531\u4f5b\u6559\u50e7\u4fa3\u9886\u5bfc\u7684\u5b97\u6559\u6cbb\u7406\u5236\u5ea6", "ja": "\u4ecf\u6559\u50e7\u4fb6\u304c\u4e3b\u5c0e\u3059\u308b\u5b97\u6559\u7684\u7d71\u6cbb\u5236\u5ea6", "es": "Un sistema de gobierno religioso liderado por monjes budistas"},
    {"en": "A legal code system modeled on Tang Dynasty China, combining penal law (ritsu) and administrative law (ryo)", "zh": "\u4eff\u7167\u5510\u671d\u4e2d\u56fd\u7684\u6cd5\u5f8b\u5236\u5ea6\uff0c\u7ed3\u5408\u5211\u6cd5\uff08\u5f8b\uff09\u548c\u884c\u653f\u6cd5\uff08\u4ee4\uff09", "ja": "\u5510\u306e\u4e2d\u56fd\u306b\u5023\u3063\u305f\u6cd5\u5178\u4f53\u7cfb\u3067\u3001\u5211\u6cd5\uff08\u5f8b\uff09\u3068\u884c\u653f\u6cd5\uff08\u4ee4\uff09\u3092\u7d44\u307f\u5408\u308f\u305b\u305f\u3082\u306e", "es": "Un sistema de c\u00f3digo legal modelado en la China de la dinast\u00eda Tang, combinando ley penal (ritsu) y ley administrativa (ryo)"},
    {"en": "A military code governing samurai conduct", "zh": "\u89c4\u8303\u6b66\u58eb\u884c\u4e3a\u7684\u519b\u4e8b\u6cd5\u5178", "ja": "\u6b66\u58eb\u306e\u884c\u52d5\u3092\u898f\u5b9a\u3059\u308b\u8ecd\u4e8b\u6cd5\u5178", "es": "Un c\u00f3digo militar que gobierna la conducta samur\u00e1i"}
  ],
  "a": 2,
  "trivia": {
    "en": "The two major codes were the Taiho Code (701) and the Yoro Code (718), which systematized Japanese governance based on Chinese legal principles.",
    "zh": "\u4e24\u5927\u6cd5\u5178\u662f\u5927\u5b9d\u5f8b\u4ee4\uff08701\u5e74\uff09\u548c\u517b\u8001\u5f8b\u4ee4\uff08718\u5e74\uff09\uff0c\u5b83\u4eec\u4ee5\u4e2d\u56fd\u6cd5\u5f8b\u539f\u5219\u4e3a\u57fa\u7840\u7cfb\u7edf\u5316\u4e86\u65e5\u672c\u7684\u6cbb\u7406\u3002",
    "ja": "\u4e8c\u5927\u6cd5\u5178\u306f\u5927\u5b9d\u5f8b\u4ee4\uff08701\u5e74\uff09\u3068\u990a\u8001\u5f8b\u4ee4\uff08718\u5e74\uff09\u3067\u3001\u4e2d\u56fd\u306e\u6cd5\u5f8b\u539f\u5247\u306b\u57fa\u3065\u3044\u3066\u65e5\u672c\u306e\u7d71\u6cbb\u3092\u4f53\u7cfb\u5316\u3057\u307e\u3057\u305f\u3002",
    "es": "Los dos c\u00f3digos principales fueron el C\u00f3digo Taiho (701) y el C\u00f3digo Yoro (718), que sistematizaron la gobernanza japonesa bas\u00e1ndose en principios legales chinos."
  }
})

# Save to temp file
with open(r"C:\Users\daigo\source\yuki\data\parts\_q11_20.json", "w", encoding="utf-8") as f:
    json.dump(new_questions, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(new_questions)} questions to temp file")
