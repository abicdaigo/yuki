import json, os

questions = [
{
  "id": "history_advanced_001",
  "q": {
    "en": "At the Battle of Sekigahara (1600), which daimyo's sudden defection to the Eastern Army proved decisive for Tokugawa Ieyasu's victory?",
    "zh": "在关原之战（1600年）中，哪位大名突然倒戈东军，对德川家康的胜利起了决定性作用？",
    "ja": "関ヶ原の戦い（1600年）で、東軍への突然の寝返りが徳川家康の勝利を決定づけた大名は誰ですか？",
    "es": "En la Batalla de Sekigahara (1600), ¿qué daimyo desertó repentinamente al Ejército del Este, resultando decisivo para la victoria de Tokugawa Ieyasu?"
  },
  "c": [
    {"en": "Kobayakawa Hideaki", "zh": "小早川秀秋", "ja": "小早川秀秋", "es": "Kobayakawa Hideaki"},
    {"en": "Shimazu Yoshihiro", "zh": "岛津义弘", "ja": "島津義弘", "es": "Shimazu Yoshihiro"},
    {"en": "Mōri Terumoto", "zh": "毛利辉元", "ja": "毛利輝元", "es": "Mōri Terumoto"},
    {"en": "Ukita Hideie", "zh": "宇喜多秀家", "ja": "宇喜多秀家", "es": "Ukita Hideie"}
  ],
  "a": 0,
  "trivia": {
    "en": "Kobayakawa Hideaki was positioned on Mt. Matsuo and his betrayal of the Western Army collapsed Ishida Mitsunari's defensive line.",
    "zh": "小早川秀秋驻守在松尾山上，他对西军的背叛导致石田三成的防线崩溃。",
    "ja": "小早川秀秋は松尾山に陣取っており、西軍への裏切りにより石田三成の防衛線が崩壊しました。",
    "es": "Kobayakawa Hideaki estaba posicionado en el Monte Matsuo y su traición al Ejército del Oeste derrumbó la línea defensiva de Ishida Mitsunari."
  }
},
{
  "id": "history_advanced_002",
  "q": {
    "en": "Which specific innovation did Oda Nobunaga employ at the Battle of Nagashino (1575) to defeat the Takeda cavalry?",
    "zh": "织田信长在长篠之战（1575年）中采用了什么具体的创新战术来击败武田骑兵？",
    "ja": "長篠の戦い（1575年）で、織田信長が武田騎馬隊を破るために用いた革新的な戦術は何ですか？",
    "es": "¿Qué innovación específica empleó Oda Nobunaga en la Batalla de Nagashino (1575) para derrotar a la caballería Takeda?"
  },
  "c": [
    {"en": "Poisoned arrows fired from hilltops", "zh": "从山顶射出毒箭", "ja": "丘の上からの毒矢", "es": "Flechas envenenadas disparadas desde colinas"},
    {"en": "Rotating volleys of arquebus fire behind wooden palisades", "zh": "在木栅栏后面进行火绳枪轮射", "ja": "木柵の後ろからの鉄砲の三段撃ち", "es": "Descargas rotativas de arcabuz detrás de empalizadas de madera"},
    {"en": "Hidden pit traps across the battlefield", "zh": "在战场上设置隐蔽的陷阱", "ja": "戦場に仕掛けた落とし穴", "es": "Trampas ocultas en el campo de batalla"},
    {"en": "War elephants imported from Southeast Asia", "zh": "从东南亚引进的战象", "ja": "東南アジアから輸入した戦象", "es": "Elefantes de guerra importados del sudeste asiático"}
  ],
  "a": 1,
  "trivia": {
    "en": "Nobunaga deployed approximately 3,000 arquebusiers in rotating ranks, revolutionizing Japanese warfare with organized volley fire.",
    "zh": "信长部署了约3000名火枪手进行轮流射击，以有组织的齐射彻底改变了日本的战争方式。",
    "ja": "信長は約3000挺の鉄砲を三段構えに配置し、組織的な一斉射撃で日本の戦術を革新しました。",
    "es": "Nobunaga desplegó aproximadamente 3,000 arcabuceros en filas rotativas, revolucionando la guerra japonesa con fuego de descarga organizado."
  }
},
{
  "id": "history_advanced_003",
  "q": {
    "en": "What was the name of the council of elders (Tairō) appointed by Toyotomi Hideyoshi to govern after his death until his son came of age?",
    "zh": "丰臣秀吉去世前任命的辅佐其子的合议制度叫什么？",
    "ja": "豊臣秀吉が死後、息子が成人するまで政治を委ねた合議体制は何と呼ばれますか？",
    "es": "¿Cómo se llamaba el consejo de ancianos designado por Toyotomi Hideyoshi para gobernar tras su muerte hasta que su hijo alcanzara la mayoría de edad?"
  },
  "c": [
    {"en": "Sankin-kōtai", "zh": "参勤交代", "ja": "参勤交代", "es": "Sankin-kōtai"},
    {"en": "Rōjū", "zh": "老中", "ja": "老中", "es": "Rōjū"},
    {"en": "Go-Tairō (Council of Five Elders)", "zh": "五大老", "ja": "五大老", "es": "Go-Tairō (Consejo de los Cinco Ancianos)"},
    {"en": "Hyōjōshū", "zh": "评定众", "ja": "評定衆", "es": "Hyōjōshū"}
  ],
  "a": 2,
  "trivia": {
    "en": "The Five Elders included Tokugawa Ieyasu, Maeda Toshiie, Ukita Hideie, Uesugi Kagekatsu, and Mōri Terumoto.",
    "zh": "五大老包括德川家康、前田利家、宇喜多秀家、上杉景胜和毛利辉元。",
    "ja": "五大老は徳川家康、前田利家、宇喜多秀家、上杉景勝、毛利輝元の五名です。",
    "es": "Los Cinco Ancianos incluían a Tokugawa Ieyasu, Maeda Toshiie, Ukita Hideie, Uesugi Kagekatsu y Mōri Terumoto."
  }
},
{
  "id": "history_advanced_004",
  "q": {
    "en": "Article 1 of the Meiji Constitution (1889) established what fundamental principle about the Emperor?",
    "zh": "明治宪法（1889年）第一条确立了关于天皇的什么基本原则？",
    "ja": "明治憲法（1889年）第1条は天皇についてどのような基本原則を定めましたか？",
    "es": "¿Qué principio fundamental sobre el Emperador estableció el Artículo 1 de la Constitución Meiji (1889)?"
  },
  "c": [
    {"en": "The Emperor shall be a constitutional figurehead", "zh": "天皇应为立宪象征", "ja": "天皇は立憲上の象徴である", "es": "El Emperador será una figura constitucional"},
    {"en": "The Emperor shall be elected by the Diet", "zh": "天皇由国会选举产生", "ja": "天皇は国会により選出される", "es": "El Emperador será elegido por la Dieta"},
    {"en": "The Empire of Japan shall be reigned over by a line of Emperors unbroken for ages eternal", "zh": "大日本帝国由万世一系之天皇统治", "ja": "大日本帝国ハ万世一系ノ天皇之ヲ統治ス", "es": "El Imperio de Japón será gobernado por una línea de Emperadores ininterrumpida por toda la eternidad"},
    {"en": "The Emperor shall share power equally with the Diet", "zh": "天皇与国会平等分享权力", "ja": "天皇は国会と平等に権力を分かち合う", "es": "El Emperador compartirá el poder equitativamente con la Dieta"}
  ],
  "a": 2,
  "trivia": {
    "en": "The Meiji Constitution was largely drafted by Itō Hirobumi after studying European constitutions, particularly the Prussian model.",
    "zh": "明治宪法主要由伊藤博文在研究欧洲宪法特别是普鲁士模式后起草的。",
    "ja": "明治憲法は伊藤博文がヨーロッパ、特にプロイセンの憲法を研究した後に起草しました。",
    "es": "La Constitución Meiji fue redactada principalmente por Itō Hirobumi tras estudiar las constituciones europeas, particularmente el modelo prusiano."
  }
},
{
  "id": "history_advanced_005",
  "q": {
    "en": "Under the Treaty of Kanagawa (1854), which two ports were opened to American ships?",
    "zh": "根据《神奈川条约》（1854年），哪两个港口向美国船只开放？",
    "ja": "日米和親条約（1854年）で、アメリカ船に開放された2つの港はどこですか？",
    "es": "Según el Tratado de Kanagawa (1854), ¿qué dos puertos se abrieron a los barcos estadounidenses?"
  },
  "c": [
    {"en": "Nagasaki and Yokohama", "zh": "长崎和横滨", "ja": "長崎と横浜", "es": "Nagasaki y Yokohama"},
    {"en": "Kobe and Osaka", "zh": "神户和大阪", "ja": "神戸と大阪", "es": "Kobe y Osaka"},
    {"en": "Shimoda and Hakodate", "zh": "下田和箱馆", "ja": "下田と箱館", "es": "Shimoda y Hakodate"},
    {"en": "Edo and Sakai", "zh": "江户和堺", "ja": "江戸と堺", "es": "Edo y Sakai"}
  ],
  "a": 2,
  "trivia": {
    "en": "Commodore Matthew Perry negotiated the treaty, effectively ending Japan's over 200 years of national seclusion (sakoku).",
    "zh": "马修·佩里准将谈判了该条约，实际上结束了日本长达200多年的锁国政策。",
    "ja": "マシュー・ペリー提督がこの条約を交渉し、日本の200年以上にわたる鎖国政策を事実上終わらせました。",
    "es": "El comodoro Matthew Perry negoció el tratado, poniendo fin efectivamente a más de 200 años de aislamiento nacional de Japón (sakoku)."
  }
},
{
  "id": "history_advanced_006",
  "q": {
    "en": "In the Treaty of Portsmouth (1905), who mediated the peace negotiations between Japan and Russia?",
    "zh": "在《朴次茅斯条约》（1905年）中，谁调解了日俄之间的和平谈判？",
    "ja": "ポーツマス条約（1905年）で、日露間の和平交渉を仲介したのは誰ですか？",
    "es": "En el Tratado de Portsmouth (1905), ¿quién medió las negociaciones de paz entre Japón y Rusia?"
  },
  "c": [
    {"en": "King Edward VII of Britain", "zh": "英国国王爱德华七世", "ja": "イギリス国王エドワード7世", "es": "El Rey Eduardo VII de Gran Bretaña"},
    {"en": "Kaiser Wilhelm II of Germany", "zh": "德国皇帝威廉二世", "ja": "ドイツ皇帝ヴィルヘルム2世", "es": "El Káiser Guillermo II de Alemania"},
    {"en": "Emperor Meiji of Japan", "zh": "日本明治天皇", "ja": "明治天皇", "es": "El Emperador Meiji de Japón"},
    {"en": "President Theodore Roosevelt of the United States", "zh": "美国总统西奥多·罗斯福", "ja": "アメリカ合衆国大統領セオドア・ルーズベルト", "es": "El Presidente Theodore Roosevelt de los Estados Unidos"}
  ],
  "a": 3,
  "trivia": {
    "en": "Roosevelt received the Nobel Peace Prize in 1906 for his mediation, though the treaty sparked the Hibiya riots in Tokyo due to Japan receiving no war indemnity.",
    "zh": "罗斯福因调解获得1906年诺贝尔和平奖，但由于日本未获得战争赔款，条约引发了东京日比谷骚动。",
    "ja": "ルーズベルトは仲介の功績で1906年にノーベル平和賞を受賞しましたが、日本が賠償金を得られなかったため日比谷焼打事件が発生しました。",
    "es": "Roosevelt recibió el Premio Nobel de la Paz en 1906 por su mediación, aunque el tratado provocó los disturbios de Hibiya en Tokio porque Japón no recibió indemnización de guerra."
  }
},
{
  "id": "history_advanced_007",
  "q": {
    "en": "Who is traditionally credited as the author of 'The Tale of Genji,' and what was her real name?",
    "zh": "《源氏物语》的传统作者是谁？她的真名是什么？",
    "ja": "『源氏物語』の作者として伝統的に知られる人物は誰で、その本名は何ですか？",
    "es": "¿Quién es tradicionalmente acreditado como autor de 'El Cuento de Genji' y cuál era su nombre real?"
  },
  "c": [
    {"en": "Sei Shōnagon; her real name is unknown", "zh": "清少纳言；真名不详", "ja": "清少納言；本名は不明", "es": "Sei Shōnagon; su nombre real es desconocido"},
    {"en": "Murasaki Shikibu; her real name is uncertain, possibly Fujiwara no Kaoriko", "zh": "紫式部；真名不确定，可能是藤原香子", "ja": "紫式部；本名は不確かだが藤原香子とも言われる", "es": "Murasaki Shikibu; su nombre real es incierto, posiblemente Fujiwara no Kaoriko"},
    {"en": "Izumi Shikibu; her real name was Ōe no Masako", "zh": "和泉式部；真名是大江雅子", "ja": "和泉式部；本名は大江雅子", "es": "Izumi Shikibu; su nombre real era Ōe no Masako"},
    {"en": "Akazome Emon; her real name was Taira no Masako", "zh": "赤染卫门；真名是平雅子", "ja": "赤染衛門；本名は平雅子", "es": "Akazome Emon; su nombre real era Taira no Masako"}
  ],
  "a": 1,
  "trivia": {
    "en": "The Tale of Genji, written around 1000-1012 CE, is often considered the world's first novel and contains 54 chapters depicting Heian court life.",
    "zh": "《源氏物语》写于约1000-1012年，通常被认为是世界上第一部长篇小说，共54章描绘了平安朝廷生活。",
    "ja": "『源氏物語』は1000年〜1012年頃に書かれ、世界最古の長編小説とされ、全54帖で平安朝の宮廷生活を描いています。",
    "es": "El Cuento de Genji, escrito alrededor de 1000-1012 d.C., es considerado a menudo la primera novela del mundo y contiene 54 capítulos que retratan la vida cortesana de Heian."
  }
},
{
  "id": "history_advanced_008",
  "q": {
    "en": "Which domain (han) led the anti-shogunate movement during the Bakumatsu and later dominated the early Meiji government along with Satsuma?",
    "zh": "幕末时期哪个藩领导了倒幕运动，后来与萨摩藩一起主导了明治初期的政府？",
    "ja": "幕末に倒幕運動を主導し、薩摩藩とともに明治初期の政府を支配した藩はどこですか？",
    "es": "¿Qué dominio (han) lideró el movimiento anti-shogunato durante el Bakumatsu y luego dominó el gobierno Meiji temprano junto con Satsuma?"
  },
  "c": [
    {"en": "Tosa", "zh": "土佐", "ja": "土佐", "es": "Tosa"},
    {"en": "Chōshū", "zh": "长州", "ja": "長州", "es": "Chōshū"},
    {"en": "Aizu", "zh": "会津", "ja": "会津", "es": "Aizu"},
    {"en": "Hizen", "zh": "肥前", "ja": "肥前", "es": "Hizen"}
  ],
  "a": 1,
  "trivia": {
    "en": "The Satchō Alliance (Satsuma-Chōshū) was brokered by Sakamoto Ryōma in 1866 and became the backbone of the Meiji Restoration.",
    "zh": "萨长同盟由坂本龙马于1866年促成，成为明治维新的核心力量。",
    "ja": "薩長同盟は1866年に坂本龍馬の仲介で成立し、明治維新の原動力となりました。",
    "es": "La Alianza Satchō (Satsuma-Chōshū) fue mediada por Sakamoto Ryōma en 1866 y se convirtió en la columna vertebral de la Restauración Meiji."
  }
},
{
  "id": "history_advanced_009",
  "q": {
    "en": "What was SCAP Directive SCAPIN-677, issued in January 1946, primarily concerned with?",
    "zh": "1946年1月发布的SCAP指令SCAPIN-677主要涉及什么内容？",
    "ja": "1946年1月に発令されたSCAP指令SCAPIN-677は、主に何に関するものでしたか？",
    "es": "¿Con qué se relacionaba principalmente la Directiva SCAPIN-677 del SCAP, emitida en enero de 1946?"
  },
  "c": [
    {"en": "Defining the areas of Japan excluded from Japanese governmental authority", "zh": "界定不属于日本政府管辖的区域", "ja": "日本政府の管轄から除外される地域の定義", "es": "Definir las áreas de Japón excluidas de la autoridad gubernamental japonesa"},
    {"en": "Dissolving the zaibatsu conglomerates", "zh": "解散财阀", "ja": "財閥の解体", "es": "Disolver los conglomerados zaibatsu"},
    {"en": "Establishing the new Japanese constitution", "zh": "制定新的日本宪法", "ja": "新日本国憲法の制定", "es": "Establecer la nueva constitución japonesa"},
    {"en": "Reforming the Japanese education system", "zh": "改革日本教育制度", "ja": "日本の教育制度改革", "es": "Reformar el sistema educativo japonés"}
  ],
  "a": 0,
  "trivia": {
    "en": "SCAPIN-677 separated the Ryukyu Islands, Bonin Islands, and other territories from Japan's administrative control, shaping postwar territorial disputes.",
    "zh": "SCAPIN-677将琉球群岛、小笠原群岛等领土从日本行政管辖中分离出来，影响了战后领土争端。",
    "ja": "SCAPIN-677は琉球諸島、小笠原諸島などを日本の行政管轄から分離し、戦後の領土問題に影響を与えました。",
    "es": "SCAPIN-677 separó las Islas Ryukyu, las Islas Bonin y otros territorios del control administrativo de Japón, moldeando las disputas territoriales de posguerra."
  }
},
{
  "id": "history_advanced_010",
  "q": {
    "en": "Which archaeological site in Aomori Prefecture is one of Japan's largest Jōmon-period settlements, dating to approximately 3900-2200 BCE?",
    "zh": "青森县的哪个考古遗址是日本最大的绳文时代聚落之一，年代约为公元前3900年至前2200年？",
    "ja": "青森県のどの遺跡が、約紀元前3900年〜前2200年の日本最大級の縄文時代の集落跡ですか？",
    "es": "¿Qué sitio arqueológico en la Prefectura de Aomori es uno de los asentamientos más grandes del período Jōmon de Japón, que data de aproximadamente 3900-2200 a.C.?"
  },
  "c": [
    {"en": "Yoshinogari", "zh": "吉野里", "ja": "吉野ヶ里", "es": "Yoshinogari"},
    {"en": "Sannai-Maruyama", "zh": "三内丸山", "ja": "三内丸山", "es": "Sannai-Maruyama"},
    {"en": "Torihama", "zh": "�的滨", "ja": "鳥浜", "es": "Torihama"},
    {"en": "Uenohara", "zh": "上野原", "ja": "上野原", "es": "Uenohara"}
  ],
  "a": 1,
  "trivia": {
    "en": "Sannai-Maruyama revealed large pit dwellings, raised-floor buildings, and evidence of long-distance trade, challenging earlier views of Jōmon society as purely nomadic.",
    "zh": "三内丸山遗址发现了大型竖穴住居、高床式建筑以及远距离贸易的证据，挑战了此前认为绳文社会纯粹为游牧生活的观点。",
    "ja": "三内丸山遺跡では大型竪穴住居や高床式建物、遠距離交易の証拠が発見され、縄文社会が純粋な遊動生活だったという従来の見方を覆しました。",
    "es": "Sannai-Maruyama reveló grandes viviendas semisubterráneas, edificios elevados y evidencia de comercio a larga distancia, desafiando las opiniones anteriores de la sociedad Jōmon como puramente nómada."
  }
}
]

# Write first 10 to file
with open(r"C:\Users\daigo\source\yuki\data\parts\history_advanced.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(questions)} questions")
