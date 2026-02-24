import json

questions = [
{
  "id": "history_advanced_011",
  "q": {
    "en": "What was the name of the six national histories (Rikkokushi) compiled during the Nara and Heian periods, and which was the first?",
    "zh": "奈良和平安时代编纂的六部国史（六国史）中，最早的一部是什么？",
    "ja": "奈良・平安時代に編纂された六国史のうち、最初のものは何ですか？",
    "es": "¿Cuál fue la primera de las seis historias nacionales (Rikkokushi) compiladas durante los períodos Nara y Heian?"
  },
  "c": [
    {"en": "Shoku Nihongi", "zh": "续日本纪", "ja": "続日本紀", "es": "Shoku Nihongi"},
    {"en": "Nihon Shoki (Nihongi)", "zh": "日本书纪", "ja": "日本書紀", "es": "Nihon Shoki (Nihongi)"},
    {"en": "Kojiki", "zh": "古事记", "ja": "古事記", "es": "Kojiki"},
    {"en": "Nihon Sandai Jitsuroku", "zh": "日本三代实录", "ja": "日本三代実録", "es": "Nihon Sandai Jitsuroku"}
  ],
  "a": 1,
  "trivia": {
    "en": "The Nihon Shoki (720 CE) is the first of the six national histories and the oldest official chronicle of Japan, written in classical Chinese.",
    "zh": "《日本书纪》（720年）是六国史之首，也是日本最古老的官方编年史，以汉文写成。",
    "ja": "『日本書紀』（720年）は六国史の最初であり、漢文で書かれた日本最古の正史です。",
    "es": "El Nihon Shoki (720 d.C.) es la primera de las seis historias nacionales y la crónica oficial más antigua de Japón, escrita en chino clásico."
  }
},
{
  "id": "history_advanced_012",
  "q": {
    "en": "Emperor Shōmu's establishment of the Tōdai-ji temple and its Great Buddha (Daibutsu) in Nara was influenced by which specific Buddhist concept?",
    "zh": "圣武天皇在奈良建立东大寺及其大佛受到了哪种具体佛教理念的影响？",
    "ja": "聖武天皇が奈良に東大寺と大仏を建立したのは、どのような仏教思想の影響を受けたものですか？",
    "es": "¿Qué concepto budista específico influyó en la construcción del templo Tōdai-ji y su Gran Buda (Daibutsu) en Nara por el Emperador Shōmu?"
  },
  "c": [
    {"en": "Pure Land Buddhism's promise of rebirth in Amida's paradise", "zh": "净土宗往生阿弥陀佛极乐世界的承诺", "ja": "浄土教の阿弥陀仏の極楽往生の教え", "es": "La promesa del Budismo de la Tierra Pura de renacer en el paraíso de Amida"},
    {"en": "Kegon (Huayan) Buddhism's vision of Vairocana Buddha as the cosmic Buddha unifying all realms", "zh": "华严宗以毗卢遮那佛为统一一切法界的宇宙佛的思想", "ja": "華厳宗の毘盧遮那仏を宇宙仏として一切を統合する思想", "es": "La visión del Budismo Kegon (Huayan) de Vairocana como el Buda cósmico que unifica todos los reinos"},
    {"en": "Zen Buddhism's emphasis on meditation and self-discipline", "zh": "禅宗强调禅定与自律的思想", "ja": "禅宗の瞑想と自己鍛錬の重視", "es": "El énfasis del Budismo Zen en la meditación y la autodisciplina"},
    {"en": "Nichiren Buddhism's focus on the Lotus Sutra", "zh": "日莲宗对法华经的重视", "ja": "日蓮宗の法華経への注力", "es": "El enfoque del Budismo Nichiren en el Sutra del Loto"}
  ],
  "a": 1,
  "trivia": {
    "en": "The Daibutsu represents Vairocana (Rushana) Buddha, and Tōdai-ji served as the head temple of the provincial temple system (kokubunji) established by Shōmu.",
    "zh": "大佛代表毗卢遮那佛（卢舍那佛），东大寺是圣武天皇设立的国分寺制度的总寺。",
    "ja": "大仏は毘盧遮那仏（盧舎那仏）を表し、東大寺は聖武天皇が設立した国分寺制度の総本山でした。",
    "es": "El Daibutsu representa al Buda Vairocana (Rushana), y Tōdai-ji sirvió como templo principal del sistema de templos provinciales (kokubunji) establecido por Shōmu."
  }
},
{
  "id": "history_advanced_013",
  "q": {
    "en": "What artificial island in Nagasaki harbor served as the sole point of European trade during Japan's sakoku period?",
    "zh": "在日本锁国时期，长崎港的哪个人工岛是欧洲贸易的唯一据点？",
    "ja": "鎖国時代、長崎港のどの人工島がヨーロッパとの唯一の貿易拠点でしたか？",
    "es": "¿Qué isla artificial en el puerto de Nagasaki sirvió como único punto de comercio europeo durante el período sakoku de Japón?"
  },
  "c": [
    {"en": "Hashima Island", "zh": "端岛", "ja": "端島", "es": "Isla Hashima"},
    {"en": "Hirado Island", "zh": "平户岛", "ja": "平戸島", "es": "Isla Hirado"},
    {"en": "Dejima", "zh": "出岛", "ja": "出島", "es": "Dejima"},
    {"en": "Enoshima", "zh": "江之岛", "ja": "江の島", "es": "Enoshima"}
  ],
  "a": 2,
  "trivia": {
    "en": "Dejima was originally built in 1636 for Portuguese traders; after their expulsion in 1639, the Dutch East India Company (VOC) was relocated there from Hirado in 1641.",
    "zh": "出岛最初于1636年为葡萄牙商人建造；1639年葡萄牙人被驱逐后，荷兰东印度公司（VOC）于1641年从平户迁至此处。",
    "ja": "出島は1636年にポルトガル商人のために建設されましたが、1639年の追放後、1641年にオランダ東インド会社（VOC）が平戸から移されました。",
    "es": "Dejima fue construida originalmente en 1636 para comerciantes portugueses; tras su expulsión en 1639, la Compañía Holandesa de las Indias Orientales (VOC) fue reubicada allí desde Hirado en 1641."
  }
},
{
  "id": "history_advanced_014",
  "q": {
    "en": "What was the 'Ōsei Fukko no Daigōrei' (Decree for the Restoration of Imperial Rule) of January 3, 1868?",
    "zh": "1868年1月3日的"王政复古大号令"是什么？",
    "ja": "慶応3年12月9日（1868年1月3日）の「王政復古の大号令」とは何ですか？",
    "es": "¿Qué fue el 'Ōsei Fukko no Daigōrei' (Decreto para la Restauración del Gobierno Imperial) del 3 de enero de 1868?"
  },
  "c": [
    {"en": "A declaration of war against the Western powers", "zh": "对西方列强的宣战", "ja": "西洋列強への宣戦布告", "es": "Una declaración de guerra contra las potencias occidentales"},
    {"en": "A decree abolishing the samurai class", "zh": "废除武士阶级的法令", "ja": "武士階級を廃止する勅令", "es": "Un decreto que abolía la clase samurái"},
    {"en": "A proclamation abolishing the shogunate and restoring direct imperial rule", "zh": "废除幕府、恢复天皇亲政的宣言", "ja": "幕府を廃止し天皇親政を復活させる宣言", "es": "Una proclamación que abolía el shogunato y restauraba el gobierno imperial directo"},
    {"en": "A treaty opening all Japanese ports to foreign trade", "zh": "向外国贸易开放所有日本港口的条约", "ja": "全ての日本の港を外国貿易に開放する条約", "es": "Un tratado que abría todos los puertos japoneses al comercio exterior"}
  ],
  "a": 2,
  "trivia": {
    "en": "The decree established the new government with the sansyoku system (three offices): President (Sōsai), Senior Councillors (Gijō), and Junior Councillors (Sanyo).",
    "zh": "该号令以三职制建立了新政府：总裁、议定和参与。",
    "ja": "この大号令により三職制（総裁・議定・参与）の新政府が樹立されました。",
    "es": "El decreto estableció el nuevo gobierno con el sistema sansyoku (tres cargos): Presidente (Sōsai), Consejeros Superiores (Gijō) y Consejeros Menores (Sanyo)."
  }
},
{
  "id": "history_advanced_015",
  "q": {
    "en": "Which Bakumatsu figure assassinated Ii Naosuke in the Sakuradamon Incident (1860)?",
    "zh": "在樱田门之变（1860年）中，谁暗杀了井伊直弼？",
    "ja": "桜田門外の変（1860年）で井伊直弼を暗殺したのは主にどの藩の浪士ですか？",
    "es": "¿Quién asesinó a Ii Naosuke en el Incidente de Sakuradamon (1860)?"
  },
  "c": [
    {"en": "Satsuma rōnin acting alone", "zh": "单独行动的萨摩浪人", "ja": "単独行動の薩摩浪士", "es": "Rōnin de Satsuma actuando solo"},
    {"en": "Chōshū loyalists", "zh": "长州勤王志士", "ja": "長州の尊王志士", "es": "Leales de Chōshū"},
    {"en": "A group of Mito rōnin (with one Satsuma samurai)", "zh": "一群水户浪人（含一名萨摩武士）", "ja": "水戸浪士の一団（薩摩藩士1名を含む）", "es": "Un grupo de rōnin de Mito (con un samurái de Satsuma)"},
    {"en": "Tosa loyalist volunteers", "zh": "土佐勤王义勇军", "ja": "土佐の勤王義勇軍", "es": "Voluntarios leales de Tosa"}
  ],
  "a": 2,
  "trivia": {
    "en": "Ii Naosuke was the Tairō (Great Elder) who had signed the Harris Treaty without imperial approval and initiated the Ansei Purge against political opponents.",
    "zh": "井伊直弼是大老，曾未经天皇批准签署了《日美修好通商条约》（哈里斯条约），并发动了安政大狱镇压政治对手。",
    "ja": "井伊直弼は大老として勅許なく日米修好通商条約に調印し、安政の大獄で政治的反対者を弾圧しました。",
    "es": "Ii Naosuke era el Tairō (Gran Anciano) que había firmado el Tratado Harris sin aprobación imperial e inició la Purga Ansei contra los opositores políticos."
  }
},
{
  "id": "history_advanced_016",
  "q": {
    "en": "During the Allied occupation, which SCAP directive ordered the dissolution of the zaibatsu holding companies?",
    "zh": "盟军占领期间，哪项SCAP指令下令解散财阀控股公司？",
    "ja": "連合国占領期間中、財閥持株会社の解体を命じたSCAP指令は何ですか？",
    "es": "Durante la ocupación aliada, ¿qué directiva del SCAP ordenó la disolución de las compañías holding de los zaibatsu?"
  },
  "c": [
    {"en": "The Dodge Line", "zh": "道奇路线", "ja": "ドッジ・ライン", "es": "La Línea Dodge"},
    {"en": "SCAPIN-244 (Dissolution of Holding Companies)", "zh": "SCAPIN-244（控股公司解散令）", "ja": "SCAPIN-244（持株会社解体令）", "es": "SCAPIN-244 (Disolución de Compañías Holding)"},
    {"en": "The Reverse Course directive", "zh": "逆转路线指令", "ja": "逆コース指令", "es": "La directiva del Curso Inverso"},
    {"en": "SCAPIN-1000 (Economic Democratization Order)", "zh": "SCAPIN-1000（经济民主化令）", "ja": "SCAPIN-1000（経済民主化令）", "es": "SCAPIN-1000 (Orden de Democratización Económica)"}
  ],
  "a": 1,
  "trivia": {
    "en": "The four largest zaibatsu — Mitsui, Mitsubishi, Sumitomo, and Yasuda — were targeted first, though many reformed as keiretsu groups after the occupation.",
    "zh": "四大财阀——三井、三菱、住友和安田——首先被解散，但许多在占领结束后以系列集团的形式重组。",
    "ja": "三井・三菱・住友・安田の四大財閥が最初に対象となりましたが、占領終了後に多くが系列として再編されました。",
    "es": "Los cuatro mayores zaibatsu — Mitsui, Mitsubishi, Sumitomo y Yasuda — fueron los primeros objetivos, aunque muchos se reformaron como grupos keiretsu después de la ocupación."
  }
},
{
  "id": "history_advanced_017",
  "q": {
    "en": "Which Heian-period practice involved retired emperors ruling from behind the scenes, known as 'cloistered rule'?",
    "zh": "平安时代哪种做法是退位天皇在幕后执政，被称为"院政"？",
    "ja": "平安時代に退位した天皇が実権を握って政治を行う制度を何と言いますか？",
    "es": "¿Qué práctica del período Heian involucraba a emperadores retirados gobernando entre bastidores, conocida como 'gobierno claustral'?"
  },
  "c": [
    {"en": "Sekkan seiji (Regency government)", "zh": "摄关政治", "ja": "摂関政治", "es": "Sekkan seiji (Gobierno de regencia)"},
    {"en": "Insei (Cloistered rule)", "zh": "院政", "ja": "院政", "es": "Insei (Gobierno claustral)"},
    {"en": "Bakufu (Tent government)", "zh": "幕府", "ja": "幕府", "es": "Bakufu (Gobierno de tienda)"},
    {"en": "Mandokoro (Administrative board)", "zh": "政所", "ja": "政所", "es": "Mandokoro (Junta administrativa)"}
  ],
  "a": 1,
  "trivia": {
    "en": "Emperor Shirakawa initiated insei in 1086 and wielded enormous power as a retired emperor for over 40 years, controlling three successive emperors.",
    "zh": "白河天皇于1086年开创院政，作为上皇掌权超过40年，控制了三代天皇。",
    "ja": "白河天皇が1086年に院政を開始し、上皇として40年以上にわたり絶大な権力を振るい、3代の天皇を支配しました。",
    "es": "El Emperador Shirakawa inició el insei en 1086 y ejerció un enorme poder como emperador retirado durante más de 40 años, controlando a tres emperadores sucesivos."
  }
},
{
  "id": "history_advanced_018",
  "q": {
    "en": "What was the primary purpose of the Taika Reforms (645 CE)?",
    "zh": "大化改新（645年）的主要目的是什么？",
    "ja": "大化の改新（645年）の主な目的は何でしたか？",
    "es": "¿Cuál fue el propósito principal de las Reformas Taika (645 d.C.)?"
  },
  "c": [
    {"en": "To establish Buddhism as the state religion", "zh": "将佛教确立为国教", "ja": "仏教を国教とすること", "es": "Establecer el budismo como religión estatal"},
    {"en": "To centralize government power under the Emperor by nationalizing land and reforming taxation", "zh": "通过土地国有化和税制改革将政权集中于天皇", "ja": "土地の国有化と税制改革により天皇のもとに政権を集中させること", "es": "Centralizar el poder gubernamental bajo el Emperador mediante la nacionalización de tierras y la reforma fiscal"},
    {"en": "To open Japan to Chinese immigration", "zh": "向中国移民开放日本", "ja": "中国からの移民を受け入れること", "es": "Abrir Japón a la inmigración china"},
    {"en": "To create a professional standing army", "zh": "建立一支职业常备军", "ja": "職業的な常備軍を創設すること", "es": "Crear un ejército profesional permanente"}
  ],
  "a": 1,
  "trivia": {
    "en": "The reforms were initiated after Prince Naka no Ōe and Nakatomi no Kamatari overthrew the powerful Soga clan in the Isshi Incident.",
    "zh": "改革是在中大兄皇子和中臣�的足在乙巳之变中推翻强大的苏我氏之后发起的。",
    "ja": "改革は中大兄皇子と中臣鎌足が乙巳の変で蘇我氏を倒した後に開始されました。",
    "es": "Las reformas se iniciaron después de que el Príncipe Naka no Ōe y Nakatomi no Kamatari derrocaron al poderoso clan Soga en el Incidente Isshi."
  }
},
{
  "id": "history_advanced_019",
  "q": {
    "en": "Which specific archaeological site in Saga Prefecture provided evidence of a large-scale Yayoi-period settlement with defensive moats?",
    "zh": "佐贺县的哪个考古遗址提供了弥生时代大规模防御性环壕聚落的证据？",
    "ja": "佐賀県のどの遺跡が、防御的な環壕を持つ弥生時代の大規模集落の証拠を提供しましたか？",
    "es": "¿Qué sitio arqueológico específico en la Prefectura de Saga proporcionó evidencia de un asentamiento a gran escala del período Yayoi con fosos defensivos?"
  },
  "c": [
    {"en": "Yoshinogari", "zh": "吉野里", "ja": "吉野ヶ里", "es": "Yoshinogari"},
    {"en": "Itazuke", "zh": "板付", "ja": "板付", "es": "Itazuke"},
    {"en": "Toro", "zh": "登吕", "ja": "登呂", "es": "Toro"},
    {"en": "Karako-Kagi", "zh": "唐古·�的", "ja": "唐古・鍵", "es": "Karako-Kagi"}
  ],
  "a": 0,
  "trivia": {
    "en": "Yoshinogari is the largest Yayoi site in Japan, featuring inner and outer moats, watchtowers, raised-floor storehouses, and burial jars, suggesting a proto-state society.",
    "zh": "吉野里是日本最大的弥生时代遗址，有内外环壕、望楼、高床式仓库和瓮棺墓葬，暗示着一个原始国家社会。",
    "ja": "吉野ヶ里は日本最大の弥生時代の遺跡で、内壕・外壕、物見櫓、高床式倉庫、甕棺墓などがあり、初期国家的な社会を示唆しています。",
    "es": "Yoshinogari es el sitio Yayoi más grande de Japón, con fosos interiores y exteriores, atalayas, almacenes elevados y urnas funerarias, sugiriendo una sociedad proto-estatal."
  }
},
{
  "id": "history_advanced_020",
  "q": {
    "en": "What was the 'Ritsuryō' system that governed Japan from the 7th to 10th centuries?",
    "zh": ""律令"制度是什么，它在7至10世纪如何治理日本？",
    "ja": "7世紀から10世紀にかけて日本を統治した「律令」制度とは何ですか？",
    "es": "¿Qué era el sistema 'Ritsuryō' que gobernó Japón del siglo VII al X?"
  },
  "c": [
    {"en": "A feudal system based on vassal-lord relationships", "zh": "基于主从关系的封建制度", "ja": "主従関係に基づく封建制度", "es": "Un sistema feudal basado en relaciones vasallo-señor"},
    {"en": "A legal code system modeled on Tang Dynasty China, combining penal law (ritsu) and administrative law (ryō)", "zh": "仿照唐朝中国的法律制度，结合刑法（律）和行政法（令）", "ja": "唐の中国に倣った法典体系で、刑法（律）と行政法（令）を組み合わせたもの", "es": "Un sistema de código legal modelado en la China de la dinastía Tang, combinando ley penal (ritsu) y ley administrativa (ryō)"},
    {"en": "A religious governance system led by Buddhist monks", "zh": "由佛教僧侣领导的宗教治理制度", "ja": "仏教僧侶が主導する宗教的統治制度", "es": "Un sistema de gobierno religioso liderado por monjes budistas"},
    {"en": "A military code governing samurai conduct", "zh": "规范武士行为的军事法典", "ja": "武士の行動を規定する軍事法典", "es": "Un código militar que gobierna la conducta samurái"}
  ],
  "a": 1,
  "trivia": {
    "en": "The two major codes were the Taihō Code (701) and the Yōrō Code (718), which systematized Japanese governance based on Chinese legal principles.",
    "zh": "两大法典是大宝律令（701年）和养老律令（718年），它们以中国法律原则为基础系统化了日本的治理。",
    "ja": "二大法典は大宝律令（701年）と養老律令（718年）で、中国の法律原則に基づいて日本の統治を体系化しました。",
    "es": "Los dos códigos principales fueron el Código Taihō (701) y el Código Yōrō (718), que sistematizaron la gobernanza japonesa basándose en principios legales chinos."
  }
},
{
  "id": "history_advanced_021",
  "q": {
    "en": "In the Heian period, what was the 'Fujiwara Sekkan' system?",
    "zh": "平安时代的"藤原摄关"制度是什么？",
    "ja": "平安時代の「藤原摂関」政治とは何ですか？",
    "es": "¿Qué era el sistema 'Fujiwara Sekkan' en el período Heian?"
  },
  "c": [
    {"en": "A trade monopoly run by the Fujiwara family", "zh": "藤原家族经营的贸易垄断", "ja": "藤原氏による貿易独占", "es": "Un monopolio comercial dirigido por la familia Fujiwara"},
    {"en": "A system where Fujiwara clansmen served as regents (Sessho and Kampaku) controlling the emperor", "zh": "藤原氏族人担任摄政（摄政和关白）控制天皇的制度", "ja": "藤原氏が摂政・関白として天皇を補佐し実権を握る制度", "es": "Un sistema donde los miembros del clan Fujiwara servían como regentes (Sessho y Kampaku) controlando al emperador"},
    {"en": "A Buddhist temple administration system", "zh": "佛教寺院管理制度", "ja": "仏教寺院の管理制度", "es": "Un sistema de administración de templos budistas"},
    {"en": "A military conscription system", "zh": "军事征兵制度", "ja": "軍事徴兵制度", "es": "Un sistema de reclutamiento militar"}
  ],
  "a": 1,
  "trivia": {
    "en": "Fujiwara no Michinaga (966-1028) was the most powerful Sekkan, famously composing a poem about the full moon reflecting his complete power over the court.",
    "zh": "藤原道长（966-1028年）是最有权势的摄关，曾吟诗"此世即吾世，如月满无缺"，表达他对朝廷的完全掌控。",
    "ja": "藤原道長（966-1028年）は最も権勢を誇った摂関で、「この世をば我が世とぞ思ふ望月の欠けたることもなしと思へば」の歌で知られます。",
    "es": "Fujiwara no Michinaga (966-1028) fue el Sekkan más poderoso, famoso por componer un poema sobre la luna llena reflejando su poder completo sobre la corte."
  }
},
{
  "id": "history_advanced_022",
  "q": {
    "en": "Which chapter of the Tale of Genji is considered particularly significant as Genji's son Kaoru becomes the protagonist?",
    "zh": "《源氏物语》中哪一部分以源氏之子薰为主角，被认为特别重要？",
    "ja": "『源氏物語』で、源氏の子・薫が主人公となる特に重要な部分は何と呼ばれますか？",
    "es": "¿Qué parte de El Cuento de Genji es considerada particularmente significativa cuando Kaoru, hijo de Genji, se convierte en protagonista?"
  },
  "c": [
    {"en": "The 'Uji Chapters' (Uji Jūjō)", "zh": "宇治十帖", "ja": "宇治十帖", "es": "Los 'Capítulos de Uji' (Uji Jūjō)"},
    {"en": "The 'Suma Chapters'", "zh": "须磨篇", "ja": "須磨の巻", "es": "Los 'Capítulos de Suma'"},
    {"en": "The 'Akashi Chapters'", "zh": "明石篇", "ja": "明石の巻", "es": "Los 'Capítulos de Akashi'"},
    {"en": "The 'Wakamurasaki Chapter'", "zh": "若紫篇", "ja": "若紫の巻", "es": "El 'Capítulo de Wakamurasaki'"}
  ],
  "a": 0,
  "trivia": {
    "en": "The Uji Chapters (chapters 45-54) shift the setting to the Uji River area and are noted for their darker, more psychological tone compared to the earlier chapters.",
    "zh": "宇治十帖（第45-54帖）将场景转移到宇治川地区，与前面的章节相比，以更加阴郁、心理化的基调著称。",
    "ja": "宇治十帖（第45帖〜第54帖）は舞台を宇治川周辺に移し、前半に比べてより暗く心理的な色彩が強いことで知られています。",
    "es": "Los Capítulos de Uji (capítulos 45-54) trasladan el escenario al área del río Uji y se destacan por su tono más oscuro y psicológico en comparación con los capítulos anteriores."
  }
},
{
  "id": "history_advanced_023",
  "q": {
    "en": "What was the 'Kenmu Restoration' (1333-1336)?",
    "zh": ""建武新政"（1333-1336年）是什么？",
    "ja": "「建武の新政」（1333-1336年）とは何ですか？",
    "es": "¿Qué fue la 'Restauración Kenmu' (1333-1336)?"
  },
  "c": [
    {"en": "Emperor Go-Daigo's brief attempt to restore direct imperial rule after overthrowing the Kamakura shogunate", "zh": "后醍醐天皇在推翻�的仓幕府后短暂恢复天皇亲政的尝试", "ja": "後醍醐天皇が鎌倉幕府を倒した後、天皇親政を復活させようとした短期間の試み", "es": "El breve intento del Emperador Go-Daigo de restaurar el gobierno imperial directo tras derrocar al shogunato de Kamakura"},
    {"en": "A Buddhist revival movement in Kyoto", "zh": "京都的佛教复兴运动", "ja": "京都での仏教復興運動", "es": "Un movimiento de renacimiento budista en Kioto"},
    {"en": "The establishment of the Muromachi shogunate", "zh": "室町幕府的建立", "ja": "室町幕府の設立", "es": "El establecimiento del shogunato Muromachi"},
    {"en": "A period of peace between the Northern and Southern Courts", "zh": "南北朝之间的和平时期", "ja": "南北朝の和平期間", "es": "Un período de paz entre las Cortes del Norte y del Sur"}
  ],
  "a": 0,
  "trivia": {
    "en": "The Kenmu Restoration failed partly because Go-Daigo favored court nobles over warriors, leading Ashikaga Takauji to rebel and establish the Muromachi shogunate.",
    "zh": "建武新政失败的部分原因是后醍醐天皇偏向公家而轻视武士，导致足利尊氏叛乱并建立室町幕府。",
    "ja": "建武の新政は後醍醐天皇が武士よりも公家を重用したことなどが原因で失敗し、足利尊氏が離反して室町幕府を開きました。",
    "es": "La Restauración Kenmu fracasó en parte porque Go-Daigo favoreció a los nobles de la corte sobre los guerreros, lo que llevó a Ashikaga Takauji a rebelarse y establecer el shogunato Muromachi."
  }
},
{
  "id": "history_advanced_024",
  "q": {
    "en": "What was the 'Tenmei Famine' (1782-1788) primarily caused by?",
    "zh": "天明大饥荒（1782-1788年）主要是由什么引起的？",
    "ja": "天明の大飢饉（1782-1788年）の主な原因は何ですか？",
    "es": "¿Qué causó principalmente la 'Hambruna Tenmei' (1782-1788)?"
  },
  "c": [
    {"en": "Invasion by Mongol forces disrupting agriculture", "zh": "蒙古军队入侵破坏农业", "ja": "モンゴル軍の侵攻による農業の混乱", "es": "La invasión de fuerzas mongolas interrumpiendo la agricultura"},
    {"en": "Volcanic eruption of Mt. Asama and cold weather patterns", "zh": "浅间山火山爆发和寒冷天气", "ja": "浅間山の噴火と冷害", "es": "La erupción volcánica del Monte Asama y patrones climáticos fríos"},
    {"en": "Intentional destruction of crops by rival domains", "zh": "敌对藩国故意毁坏庄稼", "ja": "敵対する藩による作物の意図的破壊", "es": "Destrucción intencional de cultivos por dominios rivales"},
    {"en": "A plague of locusts from the Asian mainland", "zh": "来自亚洲大陆的蝗灾", "ja": "アジア大陸からの蝗害", "es": "Una plaga de langostas del continente asiático"}
  ],
  "a": 1,
  "trivia": {
    "en": "Mt. Asama's eruption in 1783 was one of Japan's most devastating, and combined with the Laki eruption in Iceland, caused global climate disruption affecting harvests.",
    "zh": "1783年浅间山的爆发是日本最具破坏性的火山爆发之一，加上冰岛拉基火山爆发，引起了全球气候异常，影响了收成。",
    "ja": "1783年の浅間山噴火は日本史上最大級の噴火で、アイスランドのラキ火山噴火と相まって世界的な気候変動を引き起こし、収穫に影響を与えました。",
    "es": "La erupción del Monte Asama en 1783 fue una de las más devastadoras de Japón, y combinada con la erupción del Laki en Islandia, causó una disrupción climática global que afectó las cosechas."
  }
},
{
  "id": "history_advanced_025",
  "q": {
    "en": "Who was the Dutch physician who taught Western medicine at Dejima and trained Japanese students, authoring influential medical texts in the early 19th century?",
    "zh": "19世纪初在出岛教授西方医学并培训日本学生、撰写有影响力的医学文献的荷兰医生是谁？",
    "ja": "19世紀初頭に出島で西洋医学を教え日本人学生を育成し、影響力のある医学書を著したオランダ人医師は誰ですか？",
    "es": "¿Quién fue el médico holandés que enseñó medicina occidental en Dejima y formó estudiantes japoneses, escribiendo textos médicos influyentes a principios del siglo XIX?"
  },
  "c": [
    {"en": "Engelbert Kaempfer", "zh": "恩格尔伯特·坎普法", "ja": "エンゲルベルト・ケンペル", "es": "Engelbert Kaempfer"},
    {"en": "Carl Peter Thunberg", "zh": "卡尔·彼得·通贝里", "ja": "カール・ペーテル・ツンベルク", "es": "Carl Peter Thunberg"},
    {"en": "Philipp Franz von Siebold", "zh": "菲利普·弗朗茨·冯·西博尔德", "ja": "フィリップ・フランツ・フォン・シーボルト", "es": "Philipp Franz von Siebold"},
    {"en": "Jan Cock Blomhoff", "zh": "扬·科克·布洛姆霍夫", "ja": "ヤン・コック・ブロンホフ", "es": "Jan Cock Blomhoff"}
  ],
  "a": 2,
  "trivia": {
    "en": "Siebold was expelled from Japan in 1829 during the Siebold Incident for possessing prohibited maps of Japan, but later returned in 1859.",
    "zh": "西博尔德因持有日本禁止的地图在1829年的西博尔德事件中被驱逐出日本，但后于1859年返回。",
    "ja": "シーボルトは1829年のシーボルト事件で禁制の日本地図を所持していたため国外追放されましたが、1859年に再来日しました。",
    "es": "Siebold fue expulsado de Japón en 1829 durante el Incidente Siebold por poseer mapas prohibidos de Japón, pero regresó más tarde en 1859."
  }
},
{
  "id": "history_advanced_026",
  "q": {
    "en": "What was the 'Shōen' system that developed during the Heian period?",
    "zh": "平安时代发展起来的"庄园"制度是什么？",
    "ja": "平安時代に発達した「荘園」制度とは何ですか？",
    "es": "¿Qué era el sistema 'Shōen' que se desarrolló durante el período Heian?"
  },
  "c": [
    {"en": "A system of private tax-exempt estates that undermined central government authority", "zh": "一种削弱中央政府权力的私人免税庄园制度", "ja": "中央政府の権威を弱体化させた私的免税荘園の制度", "es": "Un sistema de propiedades privadas exentas de impuestos que socavó la autoridad del gobierno central"},
    {"en": "A network of fortified castles along the coast", "zh": "沿海岸线的城堡防御网络", "ja": "海岸沿いの城塞ネットワーク", "es": "Una red de castillos fortificados a lo largo de la costa"},
    {"en": "A public education system for noble children", "zh": "贵族子弟的公共教育制度", "ja": "貴族の子弟のための公教育制度", "es": "Un sistema de educación pública para hijos de nobles"},
    {"en": "A system of rotating provincial governors", "zh": "轮换制的地方总督制度", "ja": "地方長官の交代制度", "es": "Un sistema de gobernadores provinciales rotativos"}
  ],
  "a": 0,
  "trivia": {
    "en": "Shōen holders obtained immunities (fuyu and funyu) from taxation and entry by government officials, leading to a decentralization of power that eventually gave rise to the warrior class.",
    "zh": "庄园主获得了免税权（不输）和不入权（不入），导致权力去中心化，最终催生了武士阶级。",
    "ja": "荘園領主は不輸の権と不入の権を獲得し、権力の分散化が進み、やがて武士階級の台頭につながりました。",
    "es": "Los propietarios de shōen obtuvieron inmunidades (fuyu y funyu) de impuestos y entrada de funcionarios gubernamentales, llevando a una descentralización del poder que eventualmente dio origen a la clase guerrera."
  }
},
{
  "id": "history_advanced_027",
  "q": {
    "en": "During the Mongol invasions of Japan, what natural phenomenon aided the Japanese defense in both 1274 and 1281?",
    "zh": "在蒙古入侵日本期间，1274年和1281年哪种自然现象帮助了日本的防御？",
    "ja": "元寇の際、1274年と1281年の両方で日本の防衛を助けた自然現象は何ですか？",
    "es": "Durante las invasiones mongolas de Japón, ¿qué fenómeno natural ayudó a la defensa japonesa tanto en 1274 como en 1281?"
  },
  "c": [
    {"en": "Earthquakes that destroyed the Mongol fleet", "zh": "摧毁蒙古舰队的地震", "ja": "モンゴル艦隊を破壊した地震", "es": "Terremotos que destruyeron la flota mongola"},
    {"en": "Typhoons (later called 'kamikaze' or divine wind)", "zh": "台风（后来被称为"神风"）", "ja": "台風（後に「神風」と呼ばれた）", "es": "Tifones (más tarde llamados 'kamikaze' o viento divino)"},
    {"en": "Volcanic eruptions along the coast", "zh": "沿海火山爆发", "ja": "沿岸での火山噴火", "es": "Erupciones volcánicas a lo largo de la costa"},
    {"en": "Massive tidal waves (tsunami)", "zh": "大规模海啸", "ja": "大規模な津波", "es": "Enormes olas de marea (tsunami)"}
  ],
  "a": 1,
  "trivia": {
    "en": "Before the 1281 invasion, the Kamakura bakufu built a stone defensive wall (ishitsuki) along Hakata Bay, which was 20 km long and 2 meters high.",
    "zh": "在1281年入侵之前，镐仓幕府沿博多湾修建了长20公里、高2米的石砌防壁（石筑地）。",
    "ja": "1281年の侵攻の前に、鎌倉幕府は博多湾沿いに全長約20km、高さ約2mの石築地（防塁）を築きました。",
    "es": "Antes de la invasión de 1281, el bakufu de Kamakura construyó un muro defensivo de piedra (ishitsuki) a lo largo de la Bahía de Hakata, de 20 km de largo y 2 metros de alto."
  }
},
{
  "id": "history_advanced_028",
  "q": {
    "en": "What was the role of Sakamoto Ryōma in the Bakumatsu period?",
    "zh": "坂本龙马在幕末时期扮演了什么角色？",
    "ja": "幕末における坂本龍馬の役割は何でしたか？",
    "es": "¿Cuál fue el papel de Sakamoto Ryōma en el período Bakumatsu?"
  },
  "c": [
    {"en": "He served as the last shogun of the Tokugawa", "zh": "他是德川家最后一位将军", "ja": "彼は徳川家最後の将軍だった", "es": "Fue el último shogún de los Tokugawa"},
    {"en": "He led the Shinsengumi police force", "zh": "他领导了新选组警察部队", "ja": "彼は新選組を率いた", "es": "Lideró la fuerza policial Shinsengumi"},
    {"en": "He brokered the Satsuma-Chōshū Alliance and proposed the Eight-Point Plan for a new government", "zh": "他促成了萨长同盟，并提出了新政府的八策纲领", "ja": "彼は薩長同盟を仲介し、新政府のための船中八策を提案した", "es": "Medió la Alianza Satsuma-Chōshū y propuso el Plan de Ocho Puntos para un nuevo gobierno"},
    {"en": "He was the emperor who initiated the Meiji Restoration", "zh": "他是发起明治维新的天皇", "ja": "彼は明治維新を開始した天皇だった", "es": "Fue el emperador que inició la Restauración Meiji"}
  ],
  "a": 2,
  "trivia": {
    "en": "Ryōma was assassinated at the Ōmiya inn in Kyoto in 1867, just weeks before the Meiji Restoration he had helped bring about.",
    "zh": "龙马于1867年在京都近江屋被暗杀，距他帮助推动的明治维新仅数周之遥。",
    "ja": "龍馬は1867年に京都の近江屋で暗殺されました。彼が尽力した明治維新のわずか数週間前のことでした。",
    "es": "Ryōma fue asesinado en la posada Ōmiya en Kioto en 1867, solo semanas antes de la Restauración Meiji que había ayudado a lograr."
  }
},
{
  "id": "history_advanced_029",
  "q": {
    "en": "What was the 'Ansei Purge' (Ansei no Taigoku, 1858-1860)?",
    "zh": ""安政大狱"（1858-1860年）是什么？",
    "ja": "「安政の大獄」（1858-1860年）とは何ですか？",
    "es": "¿Qué fue la 'Purga Ansei' (Ansei no Taigoku, 1858-1860)?"
  },
  "c": [
    {"en": "A campaign by Ii Naosuke to suppress political opponents who criticized the signing of unequal treaties", "zh": "井伊直弼镇压批评签订不平等条约的政治反对派的运动", "ja": "不平等条約の調印を批判した政治的反対者を弾圧する井伊直弼の運動", "es": "Una campaña de Ii Naosuke para suprimir a los opositores políticos que criticaron la firma de tratados desiguales"},
    {"en": "A Buddhist monk-led rebellion against the shogunate", "zh": "佛教僧侣领导的反幕府叛乱", "ja": "仏教僧侶による幕府への反乱", "es": "Una rebelión liderada por monjes budistas contra el shogunato"},
    {"en": "A purge of Christian missionaries from Japan", "zh": "将基督教传教士逐出日本", "ja": "キリスト教宣教師の日本からの追放", "es": "Una purga de misioneros cristianos de Japón"},
    {"en": "The forced retirement of elderly daimyo", "zh": "强制年老大名退休", "ja": "高齢大名の強制隠居", "es": "El retiro forzado de daimyos ancianos"}
  ],
  "a": 0,
  "trivia": {
    "en": "The purge resulted in the execution of Yoshida Shōin, the influential Chōshū teacher whose students later led the Meiji Restoration.",
    "zh": "大狱导致吉田松阴被处死，他是有影响力的长州藩教育家，其弟子后来领导了明治维新。",
    "ja": "大獄により吉田松陰が処刑されました。松陰は長州藩の有力な教育者で、その門下生が後に明治維新を主導しました。",
    "es": "La purga resultó en la ejecución de Yoshida Shōin, el influyente maestro de Chōshū cuyos estudiantes luego lideraron la Restauración Meiji."
  }
},
{
  "id": "history_advanced_030",
  "q": {
    "en": "What was the Jinshin War (672 CE)?",
    "zh": "壬申之乱（672年）是什么？",
    "ja": "壬申の乱（672年）とは何ですか？",
    "es": "¿Qué fue la Guerra Jinshin (672 d.C.)?"
  },
  "c": [
    {"en": "A war between Japan and the Korean kingdom of Silla", "zh": "日本与朝鲜新罗王国之间的战争", "ja": "日本と朝鮮の新羅との戦争", "es": "Una guerra entre Japón y el reino coreano de Silla"},
    {"en": "A succession dispute won by Prince Ōama, who became Emperor Tenmu", "zh": "大海人皇子获胜的皇位继承之争，他后来成为天武天皇", "ja": "大海人皇子が勝利した皇位継承争いで、後に天武天皇となった", "es": "Una disputa de sucesión ganada por el Príncipe Ōama, quien se convirtió en el Emperador Tenmu"},
    {"en": "A peasant uprising against the Soga clan", "zh": "农民反对苏我氏的起义", "ja": "蘇我氏に対する農民の反乱", "es": "Un levantamiento campesino contra el clan Soga"},
    {"en": "A Buddhist-Shinto religious conflict", "zh": "佛教与神道的宗教冲突", "ja": "仏教と神道の宗教対立", "es": "Un conflicto religioso entre budismo y sintoísmo"}
  ],
  "a": 1,
  "trivia": {
    "en": "Emperor Tenmu, victorious in the Jinshin War, greatly strengthened imperial authority and is believed to have initiated the compilation of the Kojiki and Nihon Shoki.",
    "zh": "在壬申之乱中获胜的天武天皇大大加强了皇权，据信他开始了《古事记》和《日本书纪》的编纂。",
    "ja": "壬申の乱に勝利した天武天皇は皇権を大いに強化し、『古事記』と『日本書紀』の編纂を命じたとされています。",
    "es": "El Emperador Tenmu, victorioso en la Guerra Jinshin, fortaleció enormemente la autoridad imperial y se cree que inició la compilación del Kojiki y el Nihon Shoki."
  }
}
]

# Load existing
with open(r"C:\Users\daigo\source\yuki\data\parts\history_advanced.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

existing.extend(questions)

with open(r"C:\Users\daigo\source\yuki\data\parts\history_advanced.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"Total questions: {len(existing)}")
