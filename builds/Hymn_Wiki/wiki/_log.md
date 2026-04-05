---
title: "Operations Log"
type: overview
aliases: []
tags: []
created: 2026-04-04
updated: 2026-04-04
source_refs: []
related: []
status: draft
confidence: high
---

# Operations Log

Chronological record of all wiki operations.

## 2026-04-04 | setup | Wiki Scaffolding

Created Hymn Wiki build directory structure. Copied 4 source files to `raw/`. Created project spec `Hymn_Wiki.md`, tag taxonomy, and scaffolding pages. Added `hymn.yaml` schema to factory.

## 2026-04-04 | extract | Campbell Hymnal Parsing

Ran `parse_campbell.py`: extracted all 1,324 hymns with metadata (meter, topic, scripture ref, stanzas). Parsed 960 author attributions from first-line index. 667 hymns have explicit scripture references.

## 2026-04-04 | extract | KJV Bible Parsing

Ran `parse_kjv.py`: parsed 66 books, 24,200 verses into structured JSON for verse-level lookups.

## 2026-04-04 | generate | Hymn Page Generation

Ran `generate_hymn_pages.py`: created 1,324 hymn stub pages in `wiki/hymns/` with full frontmatter, hymn text from Campbell, author wikilinks, and metadata.

## 2026-04-04 | link | Bible Verse Integration

Ran `bible_linker.py`: linked 458 hymns to KJV scripture text. Created `_scripture_index.md` with 458 verse-to-hymn mappings. Built index regenerated: 1,325 pages total.

## 2026-04-04 | ingest | The Story of Our Hymns — Part I (Early Christian Hymnody)

Ingested Ryden pp. 248-1138 (Part I: Early Christian Hymnody). Created 15 entity pages and 4 concept pages.

**Entity pages created (wiki/entities/):**
- `Clement_of_Alexandria.md` — oldest known Christian hymn, "Shepherd of Tender Youth"
- `Ephrem_the_Syrian.md` — Syriac hymnist, fought heresy through congregational song
- `Hilary_of_Poitiers.md` — first Latin hymn writer
- `Ambrose_of_Milan.md` — father of Latin hymnody and Western congregational singing
- `Aurelius_Prudentius.md` — "Horace of the Christians," funeral hymn of the catacombs
- `Venantius_Fortunatus.md` — hymns of the Cross and Easter, last Ambrosian voice
- `Gregory_Nazianzen.md` — greatest Greek patristic hymnist
- `Anatolius.md` — "Fierce was the wild billow"
- `John_of_Damascus.md` — Easter hymns "The day of resurrection" and "Come, ye faithful"
- `Stephen_the_Sabaite.md` — "Art thou weary, art thou languid?"
- `Joseph_the_Hymnographer.md` — last great Greek hymnist, 9th century
- `Theodulph_of_Orleans.md` — "All glory, laud, and honor," written in prison
- `Bernard_of_Clairvaux.md` — "O sacred Head, now wounded," greatest medieval Latin writer
- `Bernard_of_Cluny.md` — "Jerusalem the golden" and two other heavenly hymns
- `Thomas_of_Celano.md` — Dies irae
- `Thomas_Aquinas.md` — Lauda Sion, closes the golden age

**Concept pages created (wiki/concepts/):**
- `Early_Christian_Hymnody.md` — overview of the first thousand years
- `Greek_and_Syriac_Hymnody.md` — the Eastern streams
- `Latin_Hymnody.md` — Western tradition from Hilary to the close of the medieval era
- `Golden_Age_of_Latin_Hymnody.md` — the twelfth and thirteenth century flowering

**Hymn page enriched:**
- `Hymn_0177_O_Sacred_Head_Now_Wounded.md` — added full historical context (Bernard/Gerhardt/Alexander/Bach transmission story)

**Index updated:** 1,349 pages total (added 24 new pages).

**Key narrative threads from Part I:**
- The role of doctrinal controversy in stimulating hymn writing (Bardesanes → Ephrem; Arians → Ambrose)
- The Gregorian reform (590 AD) that ended congregational singing for ~1,000 years
- The pattern of multiple-language transmission for medieval Latin hymns (Latin → German via Gerhardt → English via Alexander for "O sacred Head")
- John Mason Neale's 19th-century translation work as the primary channel through which Eastern and medieval hymns entered Protestant use
- No entity or concept pages yet exist for Bardesanes, Rhabanus Maurus, Adam of St. Victor, Jacobus de Benedictis — these are mentioned in concept pages but lack their own entity pages (tagged needs-expansion)

## 2026-04-04 | ingest | The Story of Our Hymns — Part II (German Hymnody)

Ingested Ryden pp. 1139-4319 (Part II: German Hymnody). Created 14 entity pages and 4 concept pages covering the full arc of German evangelical hymnody from the Reformation through the 19th-century spiritual renaissance.

**Entity pages created (wiki/entities/):**
- `Martin_Luther.md` — Father of Evangelical Hymnody; "A Mighty Fortress Is Our God"; 36 hymns; restored congregational singing
- `Philipp_Nicolai.md` — "King of Chorales" (Wake, Awake) and "Queen of Chorales" (How Brightly Shines the Morning Star); both written during a plague killing 1,300 parishioners
- `Johann_Heermann.md` — "Ah, Holy Jesus"; war-born hymns of the Thirty Years' War; ranked with Luther and Gerhardt
- `Martin_Rinkart.md` — "Now Thank We All Our God"; buried 4,000 plague victims; Germany's national Te Deum
- `Paul_Gerhardt.md` — Prince of Lutheran Hymnists; 123 hymns; "O Sacred Head Now Wounded," "All My Heart This Night Rejoices," "Now Rest Beneath Night's Shadow"
- `Joachim_Neander.md` — First great Reformed hymn-writer; "Praise to the Lord, the Almighty"; died at 30; gave his name to the Neanderthal
- `Gerhard_Tersteegen.md` — German Reformed mystic; "Thou Hidden Love of God"; "God Calling Yet"; signed covenant with God in blood
- `Count_Nikolaus_von_Zinzendorf.md` — Founder of the Moravian Brethren; 2,000+ hymns; "Jesus, Still Lead On"; inspired the modern missionary movement
- `Paul_Speratus.md` — Luther's co-laborer; "To Us Salvation Now Is Come"; wrote it in prison
- `Nicolaus_Decius.md` — Metrical Gloria in Excelsis and Agnus Dei; Luther prized both hymns highly
- `Nicolaus_Selnecker.md` — Co-author Formula of Concord; "Let Me Be Thine Forever"; "Abide with Us, O Saviour Dear"
- `Johann_Franck.md` — "Deck Thyself, My Soul, with Gladness"; pioneer of the "Jesus hymn" tradition; "Jesus, Priceless Treasure"
- `Johann_Scheffler.md` — Catholic convert (Angelus Silesius) whose mystical hymns paradoxically became Lutheran treasures; "Thee Will I Love"
- `Benjamin_Schmolck.md` — Greatest Lutheran hymn-writer of the 18th century; 1,183 hymns; "My Jesus, as Thou Wilt"; "Open Now Thy Gates of Beauty"
- `Carl_Johann_Philipp_Spitta.md` — Greatest German hymn-writer of the 19th century; "O Happy Home"; "Psalter und Harfe" went through 55 editions

**Concept pages created (wiki/concepts/):**
- `Reformation_Hymnody.md` — Overview of the whole German hymn tradition from Luther through the Reformation and its aftermath; includes Reformed psalmody context
- `Thirty_Years_War_Hymns.md` — The crucible of Lutheran hymnody 1618-1648; Heermann, Rinkart, Gustavus Adolphus, Lützen
- `Pietism.md` — The Lutheran renewal movement; Spener, Francke, Halle; Freylinghausen; Wuerttemberg school; connection to Wesleyan revival
- `Moravian_Hymnody.md` — Zinzendorf, Herrnhut, James Montgomery; influence on Wesley and the English evangelical revival
- `German_Rationalism_and_Hymnody.md` — The blight of Rationalism on German song; Gellert, Claudius, Klopstock; reaction and renaissance

**Index update:** added 19 new pages; total now approximately 1,368 pages.

**Key narrative threads from Part II:**
- The theology of congregational singing: Luther's priesthood-of-all-believers doctrine as the foundation of evangelical hymnody
- The pattern of hymns born from crisis: plague (Nicolai, 1597), war (Heermann, 1629-1634), pestilence (Rinkart, 1637), political persecution (Gerhardt, 1666), solitary illness (Hiller, 1748)
- The Reformed/Lutheran divide in hymnody: psalmody vs. hymnody, and Neander's bridge
- The Pietist movement as amplifier and eventual distorter of the Lutheran hymn tradition
- Zinzendorf and Herrnhut as the channel through which German evangelical devotion reached the Wesleys and transformed English-speaking Christianity
- The Rationalist interlude (c.1740-1820) as a period of hymnic impoverishment
- The 19th-century renaissance: Spitta, Knapp, and the return to evangelical warmth

## 2026-04-04 | ingest | The Story of Our Hymns — Parts III, IV, V (Scandinavian, English, American Hymnody)

Ingested Ryden Parts III (Scandinavian Hymnody, pp. 4320-6169), IV (English Hymnody, pp. 6170-10268), and V (American Hymnody, pp. 10269-13710). Created 33 entity pages and 6 concept pages.

**Entity pages created (wiki/entities/):**

*Scandinavian:*
- `Thomas_Kingo.md` — Denmark's first great hymnist, "poet of Easter-tide," Scottish descent (1634-1703)
- `Hans_Adolph_Brorson.md` — Danish "poet of Christmas," "Behold a host arrayed in white" as swan song (1694-1764)
- `N_F_S_Grundtvig.md` — Denmark's greatest hymnist, "poet of Whitsuntide," "Built on the Rock," preached day before death (1783-1872)
- `Johan_Olof_Wallin.md` — Archbishop of Uppsala, shaped 342 of 500 hymns in Swedish Psalm-book of 1819 (1779-1839)

*English:*
- `Isaac_Watts.md` — Father of English Hymnody; "When I survey the wondrous cross," "Joy to the world" (1674-1748)
- `Philip_Doddridge.md` — Independent minister, "O happy day," last of 20 children, died Lisbon (1702-1751)
- `Charles_Wesley.md` — Sweet Bard of Methodism, 6,500+ hymns, "Jesus, Lover of my soul" (1707-1788)
- `John_Newton.md` — Former slave-ship captain, "Amazing Grace," Olney Hymns (1725-1807)
- `William_Cowper.md` — Afflicted poet, "God moves in a mysterious way," 66 Olney hymns, holy surprise at death (1731-1800)
- `Augustus_Toplady.md` — Calvinist Anglican, "Rock of Ages," most popular English hymn, died 37 (1740-1778)
- `Reginald_Heber.md` — Missionary Bishop of Calcutta, "Holy, holy, holy," 57 hymns all still in use (1783-1826)
- `Charlotte_Elliott.md` — Invalid hymn-writer, "Just as I am," Moody's most soul-winning hymn (1789-1871)
- `Henry_Francis_Lyte.md` — Fisherfolk pastor, "Abide with me" written last Sunday, last words "Joy! Peace!" (1793-1847)
- `Sarah_Flower_Adams.md` — "Nearer, my God, to Thee," McKinley's dying prayer (1805-1848)
- `Horatius_Bonar.md` — "Sweet Singer of Scotland," 600 hymns, "I heard the voice of Jesus say" (1808-1889)
- `John_Mason_Neale.md` — Cambridge scholar, translator of ancient Greek and Latin hymns into English (1818-1866)
- `Frances_Ridley_Havergal.md` — "Consecration poet," "Take my life," died at 42 singing (1836-1879)
- `Sabine_Baring_Gould.md` — "Onward, Christian soldiers" written overnight 1865, lived to 90 (1834-1924)
- `George_Matheson.md` — Blind Scottish minister, "O Love that wilt not let me go" in minutes, 1882 (1842-1906)

*American:*
- `Thomas_Hastings.md` — Pioneer of American sacred music, 1,000+ tunes including "Toplady" and "Ortonville" (1784-1872)
- `Samuel_Francis_Smith.md` — Baptist minister, linguist in 15 languages, "America" and "The morning light is breaking" at 24 (1808-1895)
- `Ray_Palmer.md` — Congregational minister, "My faith looks up to Thee" written at 22 in a private note-book (1808-1887)
- `John_Greenleaf_Whittier.md` — Quaker abolitionist poet, "Dear Lord and Father of mankind" from 75 hymns (1807-1892)
- `Phillips_Brooks.md` — Episcopal bishop, Boston preacher, "O little town of Bethlehem" written from Christmas Eve memories (1835-1893)
- `Fanny_Crosby.md` — America's blind poet, 8,000 hymns, "Safe in the arms of Jesus," "Blessed assurance" (1823-1915)

*Works:*
- `Olney_Hymns.md` — 1779 collection by Newton (283) and Cowper (66); landmark of Anglican Evangelical hymnody

**Concept pages created (wiki/concepts/):**
- `Scandinavian_Hymnody.md` — Danish, Swedish, Norwegian Lutheran hymnody; Kingo, Brorson, Grundtvig, Wallin
- `English_Hymnody.md` — From Ken and Watts through the Victorian era; the richest tradition in the Christian world
- `Methodist_Hymnody.md` — Wesleyan revival hymnody; Charles Wesley's 6,500 hymns and the Olney collection
- `American_Hymnody.md` — From colonial psalmody through Palmer, Brooks, Whittier, and the Gospel Song movement
- `Gospel_Songs.md` — The popular revival-song tradition; Moody-Sankey campaigns; Fanny Crosby
- `Women_in_Hymnody.md` — The 19th-century rise of women hymn-writers: Elliott, Adams, Havergal, Crosby

**Index updated:** 1,418 pages total (added 34 new pages: 28 entity, 6 concept).

**Key narrative threads from Parts III-V:**
- The three Danish hymnists (Kingo/Brorson/Grundtvig) as sun/rose/bird — a full Christological/Pneumatological symbolism
- The pattern of hymns born from near-death or actual affliction: Cowper's 1773 crisis → "God moves in a mysterious way"; Lyte's last Sunday → "Abide with me"; Matheson's dark evening → "O Love that wilt not let me go"
- The Watts/Wesley comparison as the organizing question of English hymnody
- The rise of women hymn-writers in the Victorian era (Elliott, Adams, Havergal, Crosby) — all writing from real suffering
- The Toplady-Wesley controversy as the origin of "Rock of Ages" — the most popular English hymn
- Ray Palmer's private note-book poem becoming America's finest hymn
- The Olney partnership of Newton and Cowper as complementary temperaments: robust confidence vs. trembling faith

## 2026-04-04 | ingest | The Story of the Hymns and Tunes (Butterworth-Brown, 1906) — Chapters 1-7

Ingested Theron Brown and Hezekiah Butterworth, *The Story of the Hymns and Tunes* (1906), chapters 1-7, from `raw/butterworth_brown.txt`. This source supplements Ryden's *The Story of Our Hymns* with distinct biographical detail, tune histories, cultural anecdotes, and literary analysis for a largely overlapping set of hymn figures. Pages updated in two sessions.

**Existing entity pages updated with "# Musical and Thematic Context (Butterworth-Brown)" section:**
- `Augustus_Toplady.md` — thundershower-shelter story as "but one of several stories"; Queen Victoria and Prince Albert ("whispered it when he was dying"); steamer *London* sinking (Bay of Biscay, 1866); Armenian Christians massacred in Constantinople; Gen. J.E.B. Stuart at Yellow Tavern; Gladstone's Latin translation in House of Commons; tune "Toplady" by Hastings; textual variant ("tracts unknown" vs. "worlds unknown"); Unitarian substitution of "atonement lines"
- `Charlotte_Elliott.md` — Dr. Malan's words "Come just as you are"; John B. Gough's vignette of the paralytic man asking how the next verse began ("Just as I am, poor, wretched, blind — That's it, I'm blind — God help me!"); Bradbury's "Woodworth" superseding Mason's "Elliott"
- `Henry_Francis_Lyte.md` — pathos of Lyte's own tune being set aside; H.A.M. editors asking W.H. Monk to supply a tune; Monk composing "Eventide" "in ten minutes"; "Jesus I My Cross Have Taken" — six stanzas, context of unhappy church division; tunes "Autumn" (Barthelemon) and "Ellesdie" (Mozart)
- `John_B_Dykes.md` — additional tune-specific detail from Butterworth-Brown (session 1)

**New entity pages created (wiki/entities/) — 65 total across both sessions:**

*Session 1 (chapters 1-2, primarily):*
- `Lowell_Mason.md` — Father of American church music; composed "Missionary Hymn" for Heber in half an hour; 1,600+ tunes
- `Philip_Paul_Bliss.md` — Moody-Sankey revival singer; "Almost Persuaded"; died Ashtabula bridge disaster
- `Ira_D_Sankey.md` — Moody's music partner; *Sacred Songs and Solos*; composed "The Ninety and Nine" to newspaper clipping on a train
- `George_Frederick_Root.md` — Civil War song composer; "Battle Cry of Freedom"; gospel songs including "Ring the Bells of Heaven"
- `William_Bradbury.md` — American composer; "Jesus Loves Me"; tunes for "Just as I am" (Woodworth), "He Leadeth Me," and "My Hope Is Built" (Solid Rock)
- `James_Montgomery.md` — Moravian-influenced Sheffield editor; "Angels from the realms of glory"; imprisoned twice for press freedom
- `Gerhard_Tersteegen.md` — German Reformed mystic; "God Calling Yet"; signed covenant with God in blood (page updated/created)
- `Bishop_Ken.md` — Author of the morning and evening doxology; deprived of see for refusing oath to William III; died Longleat
- `John_B_Dykes.md` — Victorian church musician; composed tunes for Newman, Bonar, and many others (page updated)
- `Gustavus_Adolphus.md` — Lion of the North; sang Luther's hymn before Lützen; royal patronage of Lutheran hymnody
- `Johan_Michael_Altenburg.md` — Composed "Fear Not O Little Flock/Gustavus Adolphus' Hymn" (1632)
- `Chrétien_Urhan.md` — French violinist; composed tune "Rutherford" for Anne Ross Cousin's hymn

*Session 2 (chapters 2-7):*
- `Arcangelo_Corelli.md` — Italian violinist; "Ain" tune for Watts; mortified by confusion with Handel and brooded until death (1653-1713)
- `Sir_John_Bowring.md` — English statesman/linguist/Governor of Hong Kong; knew 100+ languages; wrote "In the Cross of Christ I Glory" and "Watchman Tell Us of the Night" (1792-1872)
- `Ithamar_Conkey.md` — American bass singer; composed tune "Rathbun" for Bowring's "In the Cross of Christ I Glory"
- `John_Keble.md` — Anglican Oxford Movement rector; wrote "Sun of My Soul" from *The Christian Year*; never tempted by wider fields (1792-1866)
- `William_Henry_Monk.md` — English organist; edited *Hymns Ancient and Modern*; arranged "Hursley" for Keble; composed "Eventide" for Lyte in ten minutes (1823-1889)
- `Frederick_William_Faber.md` — Yorkshire Oxford Movement figure; followed Newman to Rome; wrote "There's a Wideness in God's Mercy" and "Hark Hark My Soul" (1814-1863)
- `Joseph_Henry_Gilmore.md` — Rochester University professor; "jotted down" "He Leadeth Me" in Deacon Watson's parlor after Wednesday prayer meeting; found it in the hymnal at the church where he was candidating (1834-1918)
- `Robert_Lowry.md` — American Baptist minister and composer; set "He Leadeth Me," "I Need Thee Every Hour," and "Saviour Thy Dying Love" (1826-1899)
- `Annie_Sherwood_Hawks.md` — Born Hoosick NY; wrote "I Need Thee Every Hour" in 1872; Lowry added the chorus; first sung at National Baptist Sunday School Association in Cincinnati (1835-1918)
- `S_Dryden_Phelps.md` — New Haven Baptist pastor; wrote "Saviour Thy Dying Love" in 1862; Lowry's tune "Something for Jesus"; inserted by Sankey in *Gospel Hymns* No. 1 (1816-1895)
- `John_Henry_Newman.md` — Oxford Movement leader; Catholic Cardinal 1879; wrote "Lead Kindly Light" becalmed in Strait of Bonifacio 1833; tune "Lux Benigna" by Dykes (1801-1890)
- `Samuel_Medley.md` — English Baptist minister; entered Royal Navy at 18; wounded off Cape Lagos; prayed through the night for his limb; wrote "O Could I Speak the Matchless Worth" (1738-1799)
- `Johann_Georg_Nageli.md` — Swiss music publisher; adapted by Lowell Mason into "Dennis" for "Blest Be the Tie"; interpolated two bars into a Beethoven sonata without losing his friendship (1768-1836)
- `Benjamin_Beddome.md` — English Baptist pastor; served Bourton-on-the-Water 52 years; wrote "Did Christ O'er Sinners Weep"; hymns not published until 23 years after his death (1717-1795)
- `A_J_Gordon.md` — Boston Baptist pastor; found "My Jesus I Love Thee" in a London hymn-book; composed tune in "a moment of inspiration"; railway car anecdote of hushed passengers (1836-1895)
- `Samuel_Sebastian_Wesley.md` — Grandson of Charles Wesley; cathedral organist; composed "Aurelia" (later "The Church's One Foundation") (1810-1876)
- `Heinrich_Zeuner.md` — Saxon-born Boston organist; composed "Missionary Chant" for "Ye Christian Heralds Go Proclaim"; became insane 1857 and died by his own hand
- `Thomas_Kelly.md` — Dublin-born Nonconformist; wrote "On the Mountain Top Appearing" and 700+ hymns; died saying "I expect never to die" (1769-1855)
- `Harriet_Auber.md` — Secluded English hymn-writer; wrote "Our Blest Redeemer Ere He Breathed"; *Spirit of the Psalms* (1829) (1773-1862)
- `George_James_Webb.md` — Near Salisbury-born; Boston Academy of Music with Lowell Mason; composed "Webb" tune at sea en route to America (1803-1887)
- `Joseph_Hart.md` — Born London 1712; went astray; "amazing view of the sufferings of Christ" 1767; wrote "Come Ye Sinners Poor and Needy" with the unforgettable line "If you tarry till you're better / You will never come at all"; died 1768
- `Carl_Maria_von_Weber.md` — German opera composer; accidentally drank nitric acid 1806; composed tune "Wilmot" for Hart's "Come Ye Sinners"; died London aged 40 (1786-1826)
- `Helen_Maria_Williams.md` — Brilliant writer; spent much of life in London and Paris; wrote "While Thee I Seek, Protecting Power" (1762-1827)
- `Ignaz_Pleyel.md` — Haydn's "best and dearest" pupil; 24th child of a village schoolmaster; composed "Brattle Street" for Williams's hymn; founded Pleyel piano firm (1757-1831)
- `John_Cennick.md` — Born Reading; converted by sudden interior impression on a London street; worked under Wesleys, Whitefield, then Moravians; wrote "Thou Dear Redeemer Dying Lamb" and "Jesus My All to Heaven Is Gone" (1718-1755)
- `Anne_Ross_Cousin.md` — Born Melrose; wrote "The Sands of Time Are Sinking" (1857); tune "Rutherford" by Chrétien Urhan; drew on Samuel Rutherford's dying words
- `Samuel_Rutherford.md` — Scottish Covenanter/theologian; served Anworth parish; condemned for treason by Charles II; dying words "Glory shineth in Immanuel's Land" became refrain of Cousin's hymn (c.1600-1661)
- `Joseph_Addison.md` — Best English prose writer of his age; Secretary of State 1717; wrote "When All Thy Mercies O My God" in gratitude for deliverance from shipwreck off Genoa (1672-1719)
- `Jean_Jacques_Rousseau.md` — Geneva-born philosopher; composed "Greenville" (originally a love serenade from opera *Le Devin du Village*); Butterworth-Brown: "builded better than he knew...inspired, like Balaam, to utter one sacred strain" (1712-1778)
- `Catherine_Winkworth.md` — London-born translator of German hymns; *Lyra Germanica*, *Christian Singers of Germany*; translated "Fear Not O Little Flock" by Altenburg (1827-1878)
- `Phebe_Hinsdale_Brown.md` — Orphaned at 2; married house-painter; wrote "I Love to Steal Awhile Away" with baby on her lap after a neighbor's rebuke; her son became pioneer missionary to Japan (1783-1861)
- `Madame_Guyon.md` — Born Montargis; imprisoned for "Quietism" culminating in 4 years in the Bastille; wrote "My Lord How Full of Sweet Content"; said dungeon stones "looked like jewels" (1648-1717)
- `Anna_Steele.md` — Baptist minister's daughter; spent whole life in father's parsonage; wrote under pen-name "Theodosia"; her stanza "So Fades the Lovely Blooming Flower" gave birth to Oliver's tune "Federal Street" (1706-1778)
- `Hugh_Stowell.md` — Canon of Chester Cathedral; wrote "From Every Stormy Wind That Blows"; sung by eight American missionaries before their martyrdom at Cawnpore 1857; tune "Retreat" by Hastings (1799-1865)
- `Edward_Mote.md` — Born London; parents not God-fearing; converted at 16; wrote "My Hope Is Built on Nothing Less" with the refrain coming to him on his way to preach one Sabbath morning; Horsham Baptist Church 26 years (1797-1874)
- `Thomas_Moore.md` — Ireland's national poet; wrote "Come Ye Disconsolate" (~1814); Thomas Hastings revised it into a congregational hymn (1779-1852)
- `Samson_Occum.md` — Mohegan; first Native American ordained in America (1759); raised £10,000 for Moore's Indian Charity School (later Dartmouth College); wrote "Awaked by Sinai's Awful Sound"; tune "Ganges" (c.1722-1779)
- `John_Leland.md` — Baptist revival preacher; wrote "The Day Is Past and Gone" to Amzi Chapin's tune; 1801 journey to Washington on ox-team with 1,450-lb Cheshire Cheese for President Jefferson (1754-1844)
- `Peter_Cartwright.md` — Muscular Methodist circuit-preacher; sang "Then my soul mounted higher / In a chariot of fire" over a blacksmith who had defied him; the blacksmith became his friend and follower (1785-1872)
- `Henry_Hart_Milman.md` — Oxford Professor of Poetry; Dean of St. Paul's Cathedral; wrote "Ride On Ride On in Majesty" and "When Our Heads Are Bowed with Woe" (1791-1868)
- `Robert_Robinson.md` — Born Norfolk; converted by Whitefield; wrote "Come Thou Fount of Every Blessing" (~1758); later passed through many theological stages; on a stagecoach told the woman singing his hymn "Madam, I am the unhappy man who wrote that hymn many years ago" (1735-1790)
- `Ellen_Gates.md` — Youngest sister of Collis P. Huntington; wrote "Your Mission / If You Cannot on the Ocean" winter 1861-62; Lincoln twice requested it at a Senate Chamber meeting; this success first impressed Sankey with the power of evangelical solo song
- `Henry_Kemble_Oliver.md` — Massachusetts Treasurer and Adjutant General; composed tune "Federal Street" while reading Anna Steele's verse; amateur composer whose tune outlasted his public career (1800-1885)

**Index updated:** 1,476 pages total (total entities section updated from 78 to 136; new subsections added for American 18th-19th century figures, Composers, and Historical Figures)

**Key narrative threads from Butterworth-Brown chapters 1-7:**
- The "accidental sacred" pattern: Rousseau's "Greenville" (love serenade → doxology), Weber's "Wilmot" (opera music → revival hymn), Monk's "Eventide" (composed in ten minutes at editorial request)
- The missionary martyrdom vein: eight Cawnpore missionaries singing "From Every Stormy Wind" before massacre; hymn culture as comfort in extremis
- The political thread: Bowring as Governor of Hong Kong; Samson Occum raising money for Dartmouth; John Leland delivering a 1,450-lb cheese to Jefferson by ox-team
- The suffering-into-song pattern carried through women writers: Phebe Brown rebuked by a neighbor → "I Love to Steal Awhile Away"; Anna Steele's fiancé drowned day before wedding → "Father Whate'er of Earthly Bliss"; Madame Guyon in the Bastille → "My Lord How Full of Sweet Content"
- The tune-composer anecdotes: Corelli brooding to his death over a case of mistaken identity; Nageli interpolating two bars into a Beethoven sonata; A.J. Gordon composing a tune in "a moment of inspiration" after meditation
- Robert Robinson's desolate stagecoach confession as the paradigm for hymns that outlive their authors' faith

## 2026-04-04 | update | Butterworth-Brown "Musical and Thematic Context" sections — existing entity pages

Added "# Musical and Thematic Context (Butterworth-Brown)" sections to 10 additional existing entity pages from the prior Ryden ingest. Updated `source_refs` on all updated pages to include `[[The_Story_of_the_Hymns_and_Tunes]]`.

**Pages updated:**
- `Charles_Wesley.md` — "O for a Thousand Tongues" written May 17, 1739 on conversion anniversary; Peter Bohler's remark; tune "Azmon" (Glaser/Mason); Wesley's hymns as "flights"; "Lo on a Narrow Neck of Land" at Land's End; tune "Meribah" (Mason) borrowed from Lady Huntingdon; "A Charge to Keep" at camp meetings with old "Kentucky"
- `Isaac_Watts.md` — "Jesus Shall Reign" and the South Sea Islands coronation ceremony; "Joy to the World" / "Antioch" from Handel/Mason and the phenomenon of congregational gravity ("the bass falling in on the third beat as if by intuition"); "Why Do We Mourn" / Timothy Swan's "China" — "a queer medley of melody" that "made children weep"
- `Reginald_Heber.md` — Butterworth-Brown's retelling of the Wrexham Saturday afternoon story; the providential origin of "Missionary Hymn" (Lowell Mason composing it in half an hour as a young bank clerk at a lady's request); Dr. Charles Robinson's verdict: "Like the hymn it voices, it was done at a stroke"
- `Thomas_Hastings.md` — "Rock of Ages" learned "by sound" not name; Hastings's revision of Moore's "Come Ye Disconsolate"; tune "Zion" for William Williams's missionary hymn; "Ortonville" history
- `Frances_Ridley_Havergal.md` — Ecce Homo painting at Düsseldorf and its parallel effect on Zinzendorf; "Writing is praying with me"; P.P. Bliss tune details; Bliss's name correction (originally "Philipp")
- `Horatius_Bonar.md` — Hymns "coming to" Bonar on trains; study under Chalmers; Breed's "ingenious" analysis of counter-song structure; full tune survey: "Evan" (Mason from Havergal Sr.), "Athens" (Giardini), "Vox Jesu" (Spohr), Main/Abt arrangement, "Vox Dilecti" (Dykes)
- `Sarah_Flower_Adams.md` — Stead's "providential chain": Benjamin Flower jailed; Eliza Gould visiting him; their marriage producing Sarah; McKinley, Roosevelt's Rough Riders, Bishop Marvin, and the Pittsburgh forger who surrendered himself; Butterworth-Brown's defense against "evangelizing" the hymn; tune "Bethany" (Mason, 1856)
- `Sabine_Baring_Gould.md` — Precise birth/education details; Arthur Sullivan born London May 13, 1842; Mendelssohn Scholarship; knighted by Queen Victoria 1883; died November 22, 1900; "irresistible whether in band march or congregational worship"
- `John_Newton.md` — "Begone Unbelief" as "the blunt utterance of a sailor rather than the song of a poet"; tunes "Hanover" (Croft) and "Lyons" (Haydn) — the latter "more familiar — and better music"
- `Fanny_Crosby.md` — William Howard Doane (composer of "Jesus Keep Me Near the Cross") — born Preston CT 1831, 70+ inventions, Mus.D. Denison 1875; "Speed Away!" written 1890 at Sankey's request to Woodbury's melody; Crosby-Root connection at New York Institution for the Blind
- `Samuel_Francis_Smith.md` — "Not far behind Heber's *chef-d'oeuvre*"; song heard by Smith in Burma during visit to missionary son; tune "Webb" by George James Webb

## 2026-04-04 | create | Four new concept pages

Created four new concept pages from Butterworth-Brown's chapter structure and thematic content:

- `Missionary_Hymns.md` — The genre: its pre-movement origins (Watts, Williams), the three crown jewels (Heber's "From Greenland's," Smith's "Morning Light," Watts's "Jesus Shall Reign"), the providential tune story (Mason and the Savannah lady), and the role of missionary hymns in sustaining the 19th-century global enterprise
- `Revival_Hymns.md` — Pre-revival Puritan severity; the Great Awakening transformation; key hymns (Hart, Robinson, Occum, Leland, Cennick, Cartwright, Ellen Gates); the camp meeting tradition; transition to Gospel Songs
- `Christian_Ballads.md` — The intimate, experiential hymn tradition; key figures (Addison, Stowell, Anne Ross Cousin, Edward Mote, Phebe Brown, Helen Maria Williams, Madame Guyon, Tersteegen); the "accidental sacred" pattern (Rousseau, Pleyel, Weber); women hymnody and the ballad form
- `Hymn_Tunes.md` — The hymn-tune bond ("the tune has become the habit of the hymn"); origins (classical adaptation, secular sanctification, inspired composition); American and English tune composers; Butterworth-Brown's musical assessments; the "tune named for its hymn" convention

**Index updated:** 1,480 pages total (4 new concept pages added; concepts section expanded from 15 to 19)

## 2026-04-04 | update | Remaining entity page updates and tag fixes

**Additional "Musical and Thematic Context" sections added:**
- `William_Cowper.md` — "O for a Closer Walk" / Gardiner's "Dedham" and "Mear" (possibly American, New England 1726); "What Various Hindrances" / Mason's "Rockingham"; "Satan trembles when he sees the weakest saint upon his knees"
- `Philip_Doddridge.md` — "O Happy Day" and "O How Happy Are They" as the twin voices of every converts' meeting; Rimbault's tune "Happy Day" (Edward Francis Rimbault, born Soho 1816, organist at Soho Swiss Church from 16, declined Harvard professorship, died 1876)
- `Paul_Gerhardt.md` — Butterworth-Brown's concise biography in the "Hymn of Trust" context; thirty-year wandering preacher narrative; tune "Schumann" by Robert Schumann (1810-1876); Catherine Winkworth as the standard English translator
- `Gerhard_Tersteegen.md` — Precise biographical details (Mors, Westphalia; ribbon-weaver; blood covenant at 27; "Pilgrims' Cottage"; 111 hymns); Jane Borthwick as translator; Dykes's "Rivaulx" vs. Oliver's "Federal Street"; the full Federal Street story with the Peace Jubilee at Boston (ten thousand voices, 1872)

**Tag fixes (YAML frontmatter):**
- `Paul_Gerhardt.md` — removed erroneous `#` prefix from all tags
- `Gerhard_Tersteegen.md` — removed erroneous `#` prefix from all tags; also updated source_refs

## 2026-04-04 | ingest | The Story of the Hymns and Tunes (Butterworth-Brown, 1906) — Chapters 8-14

Ingested Theron Brown and Hezekiah Butterworth, *The Story of the Hymns and Tunes* (1906), chapters 8-14, from `raw/butterworth_brown.txt` (approximately lines 9296-17002). Chapters covered: Sunday School Hymns (ch. 8), Patriotic Hymns (ch. 9), Sailor's Hymns (ch. 10), Hymns of Wales (ch. 11), Field/Gospel Hymns (ch. 12), Festival and Occasional Hymns (ch. 13), Hymns of Hope and Consolation (ch. 14).

**New entity pages created (wiki/entities/) — 19 total:**

*American figures:*
- `Julia_Ward_Howe.md` — abolitionist poet who wrote "The Battle Hymn of the Republic" before dawn in a Washington hotel, November 1861 (1819-1910)
- `Philip_Phillips.md` — "The Singing Pilgrim"; decisive influence on Ira Sankey; used *Hallowed Songs* in first Moody-Sankey English missions; commissioned "Home of the Soul" from Ellen Gates (1834-1895)
- `George_Coles_Stebbins.md` — Gospel Hymns co-editor with Sankey and McGranahan; composed tunes for "There Is a Green Hill Far Away" and "We Speak of the Realms of the Blest" (1846-1945)
- `James_McGranahan.md` — Successor to P.P. Bliss as musician to Major Whittle; co-editor of Gospel Hymns (1840-1907)
- `William_H_Doane.md` — Cincinnati manufacturer and Fanny Crosby's principal musical partner; set "Rescue the Perishing," "Safe in the Arms of Jesus," "Tell Me the Old Old Story" (1832-1915)
- `Horatio_Richmond_Palmer.md` — Composed "Yield Not to Temptation" (1868); directed Church Choral Union of New York; published *Song Queen* (200,000 copies) (1834-1907)
- `Horatio_Spafford.md` — American lawyer; lost children on the Ville de Havre (November 22, 1873); wrote "It Is Well with My Soul" from that catastrophe; died Jerusalem 1888 (1828-1888)
- `Elizabeth_Clephane.md` — Scottish poet; wrote "The Ninety and Nine" (1868); died of consumption before seeing it printed; Sankey improvised its tune in Edinburgh from a clipping in his vest pocket (1830-1869)
- `Phebe_Cary.md` — Wrote "One Sweetly Solemn Thought" in a friend's back bedroom (1852); standard funeral text of the era (1824-1871)
- `Mary_Dana_Shindler.md` — Southern poet; wrote "I'm a Pilgrim and I'm a Stranger"; died Texas 1883 (1810-1883)
- `Kate_Hankey.md` — English evangelical; wrote "Tell Me the Old Old Story" and "I Love to Tell the Story" during convalescence of 1866 (1834-1911)
- `Emily_Sullivan_Oakey.md` — Language teacher at Albany Female Academy; wrote "What Shall the Harvest Be?" (1850) (1829-1883)
- `Anna_Warner.md` — Lived at West Point, conducted Sunday school for cadets; wrote "Jesus Loves Me" and "One More Day's Work for Jesus" (1820-1915)
- `Joseph_Scriven.md` — Irish-born Canadian; bride-to-be drowned eve of their wedding; consecrated life to Christ; wrote "What a Friend We Have in Jesus" (1820-1886)
- `John_Pierpont.md` — Unitarian minister and patriotic poet; wrote "Warren's Address at Bunker Hill" (1785-1866)
- `Henry_Kirke_White.md` — English poet; died at barely twenty; conversion story (the Almond night); wrote "When Marshalled on the Nightly Plain" (1795-1806)

*English figure:*
- `Jemima_Thompson_Luke.md` — English educator; wrote "I Think When I Read That Sweet Story of Old" in a stage-coach (1841); set to more different tunes than almost any Sunday-school hymn (1813-1906)
- `Cecil_Frances_Alexander.md` — Irish poet; *Hymns for Little Children* (1848); wrote "There Is a Green Hill Far Away," "Once in Royal David's City," "All Things Bright and Beautiful" (1823-1895)

*Welsh figures:*
- `Thomas_Williams_Welsh.md` — Welsh Calvinistic Methodist of Glamorganshire; "Unto Thy Presence Coming" and "O Had I the Wings of a Dove" (1761-1844)
- `David_Charles.md` — Calvinist Methodist minister of Carmarthen; "heavenly-minded" preacher; "The Heights of Fair Salem Ascended" (1762-1834)
- `Morgan_Rhys.md` — Welsh schoolmaster-preacher; friend of William Williams of Pantycelyn; "Lo! A Saviour for the Fallen" (1716-1779)
- `Thomas_Jones_of_Denbigh.md` — Welsh Calvinistic Methodist minister; "Early to Bear the Yoke Excels" (1756-1820)
- `William_Rees_Welsh.md` — Welsh poet Gwilym Hiraethog; wrote "Dyma Gariad Fel y Moroedd" (Love Unfathomed as the Ocean), the great Welsh hymn of divine love (1802-1883)

**New concept pages created (wiki/concepts/) — 4 total:**
- `Welsh_Hymnody.md` — Full arc from medieval roots through the 18th-century Calvinistic Methodist revival (Williams, Ann Griffiths) to the 1859 and 1904-5 revivals; Welsh tune tradition; characteristic features of Welsh hymnody
- `Sunday_School_Hymns.md` — From Clement's Hymn (c. 200) through Jemima Thompson Luke, Dorothy Thrupp, Cecil Frances Alexander, Fanny Crosby, W.O. Cushing, H.R. Palmer, and the Gospel Hymns composers; the children's hymn as a distinct genre
- `Patriotic_Hymns.md` — Star-Spangled Banner, My Country 'Tis of Thee, Battle Hymn of the Republic, Hail Columbia, Keller's American Hymn, Kipling's Recessional, God Bless Our Native Land; the prophetic and the civic in American hymnody
- `Hymns_of_Consolation.md` — Jerusalem the Golden, Phebe Cary's "One Sweetly Solemn Thought," Ellen Gates's "Home of the Soul," Horatio Spafford's "It Is Well with My Soul," Margaret Mackay's "Asleep in Jesus," Fanny Crosby's "Safe in the Arms of Jesus"; the theology and practice of consolation hymnody

**Existing entity pages updated:**
- `George_Frederic_Handel.md` — Added sections on: "Antioch" tune for "Joy to the World" (Messiah adaptation via Lowell Mason); Handel's blindness at age 68 (1753); "Dead March from Saul" as standard English funeral music; "Christmas" tune from opera *Ciroe* (1738) for Doddridge's "Awake My Soul"

**Index updated:** 1,507 pages total (added 27 new pages: 23 entity, 4 concept; Welsh section added to entities; Welsh figures and four new concepts added to index listings)

## 2026-04-04 | synthesis | Synthesis and Timeline Pages Created

Created 5 synthesis pages and 1 timeline page.

**Synthesis pages created (wiki/synthesis/) — 5 total:**
- `History_of_Christian_Hymnody.md` — Sweeping executive summary from apostolic age to the gospel song era; traces Greek/Syriac, Latin, Reformation, English, and American streams; wikilinked throughout to era concept pages and key figures
- `The_Great_Hymn_Writers.md` — Comparative analysis of Luther, Gerhardt, Watts, Wesley, and Crosby; what made each great; how they differ; comparison table by era, tradition, output, and distinctive gift
- `Women_Who_Shaped_Hymnody.md` — Synthesis celebrating Havergal, Crosby, Elliott, Adams, Warner, Alexander, and ten additional women writers; examines the pattern of great hymns emerging from constrained and suffering lives
- `Hymns_Born_from_Suffering.md` — Cross-cutting analysis of the consistent pattern of great hymns emerging from plague (Nicolai, Rinkart), war (Heermann, Gerhardt), blindness (Crosby), grief (Spafford, Matheson, Lyte), and invalidism (Elliott, Adams); includes summary table
- `The_Bible_in_Hymnody.md` — How Scripture shaped the hymn tradition: psalm paraphrases (Watts), Reformation pauline hymns, Gospel narrative hymns (Christmas, Easter), prophetic imagery (Heber); links to `_scripture_index`

**Timeline page created (wiki/timelines/) — 1 total:**
- `Christian_Hymnody_Timeline.md` — Chronological timeline from c. 100 AD to 1930; organized by century with Markdown tables; covers all major figures, movements, and publications; links to all relevant entity, concept, and synthesis pages

**Index updated:** 1,513 pages total (added 6 new pages: 5 synthesis, 1 timeline; synthesis and timelines sections added to index)

## 2026-04-04 | lint | Final Quality Pass

Ran `lint_wiki.py`, `build_index.py`, `orphan_check.py`, and `tag_report.py`. Fixed:
- Added `hymn` to lint script's valid types
- Fixed 18 files with broken YAML frontmatter (unquoted `#` tags)
- Fixed 164 files with improperly formatted tag arrays
- Fixed double-hash (`##`) tag artifacts from batch fixes
- Added 20+ new legitimate tags to taxonomy (composer roles, additional traditions, themes)
- Resolved all rogue tag substitutions (`#tradition-evangelical` -> `#tradition-congregational`, etc.)

**Final stats:** 0 errors, 1,889 warnings (mostly dead wikilinks -- Obsidian fuzzy matching handles these), 885 info items (orphan hymn stubs awaiting enrichment). 1,517 pages indexed across 7 types.

## 2026-04-04 | create | 7 Missing Concept Pages

Created 7 concept pages linked from `_overview.md` that were missing from `wiki/concepts/`:
- `Medieval_Hymnody.md` --- 7th-15th century monastic hymnody, sequences, Bernard of Clairvaux, Bernard of Cluny, Thomas Aquinas, Thomas of Celano
- `Post-Reformation_Hymnody.md` --- 17th century: Gerhardt, Thirty Years' War hymns, early Pietism, the chorale tradition after Luther
- `18th_Century_Hymnody.md` --- Watts, the Wesleys, Great Awakening, Olney Hymns, Toplady
- `19th_Century_Hymnody.md` --- Golden age: Fanny Crosby, Havergal, Heber, Oxford Movement, gospel songs, American hymnody
- `20th_Century_Hymnody.md` --- Brief page noting wiki coverage ends ~1930; legacy of 19th century tradition
- `Lutheran_Hymnody.md` --- Complete Lutheran tradition: Luther through Gerhardt, Pietism, Scandinavian Lutheran hymnody (Kingo, Brorson, Grundtvig, Wallin), Winkworth translations
- `Anglican_Hymnody.md` --- Church of England tradition: Ken, metrical psalms, Olney Hymns, Heber, Oxford Movement, Hymns Ancient and Modern, Neale translations

## 2026-04-04 | create | Navigation and Polish

- Created 4 type-overview pages: `Hymns_Overview.md`, `People_Overview.md`, `Concepts_Overview.md`, `Synthesis_Overview.md`
- Created `Famous_Hymns.md` with ~70 linked hymns organized by category
- Updated `_overview.md` with working Browse by Type links and Featured section
- Added navigation breadcrumbs to all 1,517 pages via `add_navigation.py`
- Fixed critical issues: deleted 2 empty root-level conflicting files, fixed Amazing Grace stanza numbering, fixed Hymn 47 empty page, added Anne Steele alias, corrected Fanny Crosby birth year, fixed Abide with Me tag
- Created `Alexander_Campbell.md` entity page

## 2026-04-04 | output | Quartz HTML Site

Generated static HTML site via Quartz v4. 4,704 HTML files, 71 MB. Configured with `enableSPA: false` for local server compatibility. Created `_serve.py` (clean-URL Python server) and `Start_Hymn_Wiki.bat` launcher. Site copied to `outputs/site/`.

## 2026-04-04 | release | Version 1.0.0

Build approved. Updated documentation: `Hymn_Wiki.md` (self-improvement log), `Template.md` (v1.1.0, lessons from first build), `CLAUDE.md` (v1.1.0, Quartz workflow, custom types, navigation standing orders). Final page count: 1,530+.

## 2026-04-05 | ingest | Baptist Hymn Writers and Their Hymns (Burrage, 1888)

Ingested Henry S. Burrage, *Baptist Hymn Writers and Their Hymns* (1888), from `raw/Burrage.txt` (36,616 lines, OCR scan). Full source summary page already created at `wiki/sources/Baptist_Hymn_Writers.md`. Pages created and updated across two sessions.

**New entity pages created (wiki/entities/) — 16 total:**
- `John_Bunyan.md` — Bedford tinker; Pilgrim's Progress; Bedford jail hymns; 1628-1688
- `Benjamin_Keach.md` — Introduced hymn-singing to Baptist worship; pillory at Aylesbury; *Scriptural Melody* (1691); 1640-1704
- `John_Rippon.md` — 63-year Carter Lane/New Park Street pastorate; *Selection of Hymns* (1787); Baptist Annual Register; Spurgeon's predecessor; 1751-1836
- `Samuel_Pearce.md` — Co-founder Baptist Missionary Society at Kettering (1792); aspired to India; 1766-1799
- `William_Gadsby.md` — Ribbon weaver converted after witnessing execution; 40-year Manchester pastorate; Selection of Hymns grew to 1,100+; 1773-1844
- `Charles_Spurgeon.md` — Metropolitan Tabernacle; *Our Own Hymn Book* (1866) with 1,129 hymns; Robert Robinson's pastoral successor; 1834-1892
- `Adoniram_Judson.md` — First American Baptist foreign missionary; Burma mission; Burmese Bible completed 1834; *Come Holy Spirit Dove Divine*; 1788-1850
- `Sarah_B_Judson.md` — Burma missionary; married Judson after Boardman's death; died at St. Helena 1845; 1803-1845
- `Emily_C_Judson.md` — "Fanny Forester" pen name; third wife of Adoniram Judson; tribute poem to Sarah at St. Helena; 1817-1854
- `John_Newton_Brown.md` — New Hampshire Declaration of Faith; Encyclopaedia of Religious Knowledge; American Baptist Publication Society editor; 1803-1868
- `Basil_Manly_Jr.md` — *Baptist Psalmody* (1850) with father; SBTS professor; Seminary Hymn sung at every commencement since 1860; 1825-
- `Lydia_Baxter.md` — Invalid hymn-writer; "Take the Name of Jesus with You"; *Gems by the Wayside* (1855); Maggie Lindsay story; 1809-1874
- `Gottfried_Lehmann.md` — First Berlin Baptist church pastor; baptized in lake near Berlin (1837); six hymns in *Die Glaubensharfe*; 1799-1882
- `Julius_Kobner.md` — Rabbi's son; Danish-German Baptist pioneer; compiled *Glaubensstimme*; known in six languages; 1807-1884
- `Augustus_Rauschenbusch.md` — Rochester Seminary German Dept. professor; compiled *Pilgerharfe*; father of Walter Rauschenbusch; 1816-
- `Walther_Rauschenbusch.md` — (wikilink created in Augustus page)

**New concept page created (wiki/concepts/):**
- `Anabaptist_Hymnody.md` — 16th-century martyr hymns; the *Auss Bundt* (1583); Felix Mantz, Michael Sattler, and other Anabaptist hymn-writers; character of the hymns (no revolutionary content); bridge to Baptist hymnody

**Existing entity pages updated with "## Baptist Tradition Context (Burrage)" sections:**
- `Robert_Robinson.md` — Cambridge ordination 1761; University hearers; 600-seat building; Spurgeon connection; Unitarian controversy addressed; Robert Hall's epitaph; "Mighty God While Angels Bless Thee" origin
- `Anna_Steele.md` — Corrected birth year (1716); father William Steele as unsalaried pastor; father's diary entries; Hatfield's "female Poet of the Sanctuary" assessment; 100+ hymns; dying words; tombstone inscription
- `Samuel_Medley.md` — Grandfather's Eagle Street Baptist connection; dying words; publication history 1786-1800; John Stanford's NY collection; "Awake My Soul" composition story; third notable hymn
- `John_Fawcett.md` — Frontispiece portrait; birth date clarification (OS/NS); Whitefield sermon text; detailed wagon-loading dialogue; additional hymn list; Brown University D.D. (1811); declined Bristol Academy presidency (1793)
- `Benjamin_Beddome.md` — Birth at Henley-in-Arden; father John Beddome; conversion August 7 1737; ordination with Joseph Stennett preaching; prophetic 1742 verses; London call refused by congregation; son's death day / "My times are in thy hand" coincidence; died writing a hymn; 1818 collection; Robert Hall preface; Montgomery's "Greek epigram" assessment
- `Samuel_Stennett.md` — Genealogy corrected (great-grandson of Edward); family dynastic detail; education at Stepney and Mile End; ordination June 1 1758; Saturday service at grandfather's church for 20 years; scholarly publications; Aberdeen D.D. 1763; John Howard's letter from Smyrna; burial in Bunhill Fields
- `Edward_Mote.md` — Born Upper Thames Street; parents kept public house; apprenticed cabinetmaker; conversion 1813; baptized November 1 1815; pastor Horsham from 1852 (not earlier); chapel gift refused; never missed a Sunday; Holborn Hill (on way to work, not to preach); death words
- `Samuel_Francis_Smith.md` — Institutional career details; Harvard classmate of Holmes; ordination 1834; The Psalmist (1843) with Baron Stow; "Yes My Native Land" origin story; son D.A.W. Smith at Rangoon; ~100 hymns total; "Today the Savior Calls" from Schiller
- `Robert_Lowry.md` — Born Philadelphia 1826; baptized by Geo. B. Ide; Bucknell valedictory 1854; full pastoral career; chapel offered/refused anecdote; "Shall We Gather" composed July 1864 lying on a lounge in Brooklyn; Alexandria hospital story; Bradbury succession to Biglow and Main; publication list with circulation figures
- `John_Leland.md` — Death date corrected (1841, not 1844); Northbridge baptism; Virginia ordination; 3,009 sermons, 700 baptisms in Virginia; 1,352 total baptisms by 1821; "Christians If Your Hearts Be Warm" origin story; Duffield's "Ambrosian simplicity" assessment; Vicksburg siege diary entry
- `Benjamin_Beddome.md` — (see above)
- `A_J_Gordon.md` — Brown/Newton career details; Jamaica Plain and Clarendon Street; Moody partnership; books and publications; "Whom Shall I Send?" written at Northfield for college missionary students (1886)
- `William_H_Doane.md` — Born Preston CT 1832; Woodstock Academy; business career; converted 1847; baptized 1851; Mount Auburn Baptist Church; musical development from age 6; instructors; Norwich Harmonic Society; full publication list with Lowry; Mus.D. Denison 1875
- `Joseph_Henry_Gilmore.md` — Brown University highest honors 1858; Newton Theological Institution; Hebrew instructor; ordination 1862; Fisherville NH; governor's secretary 1863-64; Rochester career; full first-person account of hymn composition; Bradbury/Watchman connection; Swedish refrain
- `Annie_Sherwood_Hawks.md` — Born Hoosick NY 1835; Brooklyn Baptist; Lowry discovering her gift ~1868; first sung November 20 1872 at National Baptist Sunday School Convention Cincinnati; prison chaplain Batt / Mr. B's home dedication story; other hymns listed
- `S_Dryden_Phelps.md` — Suffield conversion; Brown University 1840-44; Yale Theological; New Haven pastorate 28 years (1,217 united, 615 by baptism); Madison D.D. 1854; Providence; Christian Secretary editor 1876-88; Brown trustee 1879; Plymouth Collection contributions; book publications
- `Oliver_Holden.md` — Holden's Baptist connections; 5th from Richard Holden (1634); carpenter trade; Charlestown music store; hymnological evidence from Rev. Bird's book; list of hymn first lines; "They who seek a throne of grace" as surviving hymn; "Coronation" composed 1792 confirmed

**Source refs updated** on all above pages to include `[[Baptist_Hymn_Writers]]`.

**Walther Rauschenbusch** — cross-referenced from Augustus Rauschenbusch page; full page to be created if/when Social Gospel concept added to wiki scope.

**Pages not updated** (not covered by Burrage, being non-Baptist writers): Thomas Hastings, George Frederick Root, William Bradbury, Lowell Mason, James Montgomery, Thomas Kelly, Kate Hankey, Horatio Spafford, Elizabeth Clephane, Joseph Scriven, Anna Warner, Cecil Frances Alexander, Catherine Winkworth, Peter Cartwright, Phebe Hinsdale Brown, Philip Doddridge.

## 2026-04-05 | ingest | American Writers and Compilers of Sacred Music (Metcalf, 1925)

Ingested Frank J. Metcalf's 15,981-line biographical dictionary of American tune composers. Source file: `raw/Metcalf.txt`.

**New entity pages created (wiki/entities/):**
- `John_Tufts.md` — First American tune book compiler (c. 1721), letter-notation system
- `James_Lyon.md` — Urania (1761), "Whitefield's" tune (earliest American printing of what became "America"), minister at Machias Maine
- `Andrew_Law.md` — Shape-note notation innovator, tune "Mear"
- `Justin_Morgan.md` — Singing master and Morgan horse breeder, tune "Montgomery"
- `Simeon_Butler_Marsh.md` — Tune "Martyn" for "Jesus, Lover of My Soul" (1834)
- `Samuel_A_Ward.md` — Tune "Materna" (originally for "O Mother, Dear Jerusalem"; later "America the Beautiful")
- `Stephen_Collins_Foster.md` — 29 sacred pieces in Atheneum Collection (1863), attended Black camp meetings for research
- `George_Hood.md` — First History of Music in New England (1846)
- `George_K_Jackson.md` — Approved Lowell Mason's first manuscript for Handel and Haydn Society
- `Gottlieb_Graupner.md` — Cofounded Handel and Haydn Society
- `John_Wyeth.md` — Repository of Sacred Music (1810, 1813), shape-note tradition
- `Isaac_Baker_Woodbury.md` — Prolific mid-19th-century compiler (died age 39)
- `John_Zundel.md` — Tune "Beecher"/"Love Divine, All Loves Excelling," Plymouth Church Brooklyn organist 28 years
- `Henry_Wellington_Greatorex.md` — Chant and doxology compiler
- `Jonathan_Call_Woodman.md` — Tune "State Street," George F. Root's brother-in-law
- `Virgil_Corydon_Taylor.md` — Mayflower-descended singing school master
- `Marcus_M_Wells.md` — Tune "Holy Spirit, Faithful Guide" (words and music, written October 1858)
- `Mathias_Keller.md` — "The American Hymn" (Speed Our Republic)
- `Daniel_Read.md` — Tunes "Lisbon" and "Windham" (found in 7 of recent hymnals)
- `Timothy_Swan.md` — Tune "China" (composed 1790), hat-maker composer
- `Samuel_Holyoke.md` — Columbian Repository of Sacred Harmony (1802), 734 tunes
- `Jeremiah_Ingalls.md` — Tune "Northfield" (composed while waiting for dinner)
- `Benjamin_Carr.md` — Musical Fund Society of Philadelphia, possibly first American opera
- `Anthony_Philip_Heinrich.md` — "Father Heinrich," Bohemian-born symphonic nationalist, lived among Kentucky Indians
- `Lewis_Hartsough.md` — Tune "Welcome Voice"/"I Am Coming, Lord" (sung in WWI trenches), Utah Mission organizer
- `William_G_Fischer.md` — Tune "I Love to Tell the Story," directed 1,000-voice choir at Moody-Sankey meetings

**Existing entity pages updated** with `## Musical Context (Metcalf)` section:
- `Thomas_Hastings.md` — Pseudonyms, albino detail (he and two brothers), tune survey (Toplady in all 12 hymnals, Ortonville in 10, Retreat in 9, Zion in 8)
- `William_Billings.md` — Family Bible source for 1746 birth date, Lucy Swan marriage at Stoughton singing school, Stoughton Musical Society (1786), Samuel Adams friendship, death notice from Columbian Centinel
- `Oliver_Holden.md` — Birth date September 18 1765, Charlestown real estate, 8 terms in Massachusetts House, full bibliography of 7 collections (1792-1803), Metcalf's last-words account
- `Lowell_Mason.md` — Savannah bank clerk years, Jackson's approval of manuscript, anonymous publication story, Handel and Haydn Collection details ($30,000+ each), Boston Academy 1832, public school music 1838, Musical Convention 1834, Yale library bequest, first US Doctor of Music (1855), major publication circulation figures
- `George_James_Webb.md` — Born June 24 1803 Wiltshire, Salisbury/Falmouth study, fortuitous ship change to Boston, Old South Church, Webb-Mason family connection (daughter Mary/son William), bibliography, Root's tribute, "Goodwin"→"Webb" name history, 26-hymnal survey
- `William_Bradbury.md` — Born October 6 1816 York Maine, organ-key-pulling anecdote, Fanny Crosby as blind pupil, Leipzig study/overworked arm, attended Mendelssohn's funeral November 4 1847, 59 books in 26 years, "Woodworth" in all 10 hymnals, 2M+ copies, died January 7 1868 Montclair NJ
- `George_Frederick_Root.md` — Born August 30 1820 Sheffield MA, North Reading, Mason/Webb/Baker training, married Mary Olive Woodman August 1845, taught blind Fanny Crosby at NY Institution for the Blind, Normal Musical Institutes 1853, Chicago/Root and Cady 1859, 1871 fire, Doctor of Music 1872, "Shining Shore" origin story, died August 6 1895 Bailey's Island ME
- `Henry_Kemble_Oliver.md` — Born November 24 1800 Beverly MA, Dartmouth graduate 1818, "Federal Street" composed 1832 to Anna Steele's words, Mason discovered it 2 years later, "Merton" composed during sermon, 36 years as organist, 24 years schoolteacher, full public career (Adjutant General, mayor, state treasurer, Bureau of Labor), died August 12 1885 on Federal Street
- `Heinrich_Zeuner.md` — Born September 20 1795 Eisleben, came to America c.1824, "Missionary Chant" inspiration (Boston Common moonlit evening), "Hummel" named for teacher, oratorio destruction story, Ancient Lyre went through 20+ editions, death by suicide November 7 1857
- `Horatio_Spafford.md` — Born October 20 1829, Ville-du-Havre collision details (November 22 1873, 226 drowned), Mrs. Spafford's telegram "Saved alone," hymn written on return to Chicago, Jerusalem colony founded September 26 1881, Spafford died seven years to the day from landing
- `John_Henry_Newman.md` — Metcalf's analysis of musical difficulty of "Lead, Kindly Light"; "Apologia pro Vita Sua" quote; June 16 1833 composition date; first published in British Magazine; Carnegie waking-hymn anecdote; word-count analysis (130 words, only 16 multisyllabic)

**Source summary page updated:** `wiki/sources/American_Writers_and_Compilers_of_Sacred_Music.md` — expanded from draft to complete status with full entity page cross-reference list.

**Tune-to-hymn data extracted:** `wiki/_metcalf_tune_data.json` — 52 tune-to-hymn pairing records covering composers from Holden through Fischer.

**Pages NOT updated** (not covered as chapter subjects by Metcalf, being British hymnwriters or text-only authors): Samuel Sebastian Wesley, Horatio Richmond Palmer, William H. Doane, Ira Sankey, George Coles Stebbins, James Montgomery, Philip Paul Bliss.

## [2026-04-05] ingest | The English Hymn (Benson, 1915)

Source: Louis F. Benson, *The English Hymn: Its Development and Use in Worship* (1915), C:\Wiki_Factory\builds\Hymn_Wiki\raw\Benson.txt (34,910 lines)

**New entity pages created (5):**
- Richard_Baxter.md --- ejected Presbyterian minister; advocate for hymn-singing pre-Watts
- John_Playford.md --- parish clerk; first attempt to introduce hymns into Church of England (1671)
- Rowland_Hill.md --- Surrey Chapel; Calvinistic Evangelical; 50 years popularizing hymn-singing
- James_Martineau.md --- Unitarian minister; shaped British Unitarian hymnody 1840-1900
- Henry_Ward_Beecher.md --- Plymouth Collection (1855); transformed American congregational singing

**Entity pages updated (2):**
- Benjamin_Keach.md --- added Benson section on the Singing Controversy
- Thomas_Ken.md --- added Benson section on Ken's place in Anglican hymnodic history

**New concept pages created (7):**
- Baptist_Hymnody.md --- from General Baptist opposition through Keach, Rippon, and American Baptists
- Presbyterian_Hymnody.md --- the Psalmody Controversy, ejected Presbyterians, American adoption
- Hymns_Ancient_and_Modern.md --- the landmark Anglican hymnal (1861); Dykes; Oxford movement expression
- Camp_Meeting_Hymns.md --- Kentucky Revival 1800; refrain structure; Cumberland Presbyterian Church
- Oxford_Movement_and_Hymnody.md --- Keble, Newman, Neale, HAM; institutional spread to Nonconformity
- Unitarian_Hymnody.md --- Martineau's English collections; American literary standard; Holmes, Longfellow
- Gospel_Hymn_Movement.md --- YMCA origins, Moody-Sankey, Bliss, deterioration, church impact

**Concept pages updated with Institutional History (Benson) sections (6):**
- Anglican_Hymnody.md, Methodist_Hymnody.md, Moravian_Hymnody.md
- Gospel_Songs.md, American_Hymnody.md, English_Hymnody.md, Revival_Hymns.md

_index.md updated; 13 new pages added (5 entities, 7 concepts, 1 source already existed).

## 2026-04-05 | ingest | English Hymns: Their Authors and History (Duffield, 1886)

Ingested Samuel Willoughby Duffield, *English Hymns: Their Authors and History* (1886) from `raw/Duffield.txt` (38,337 lines, OCR scan). Main body: lines 236-31,507. Processing script: `factory/scripts/process_duffield_v2.py`.

**Data file created:** `wiki/_duffield_hymn_data.json` — 1,081 hymn entries with author, composition date, composition story, first published, textual notes, anecdotes, tune info, scripture basis.

Top authors: Watts (133), C. Wesley (35), Newton (30), Doddridge (29), Montgomery (28), Kelly (25), Bonar (21), Steele (19), Palmer (14), Caswall (12), Heber (12), F.R. Havergal (12), Neale tr. (12), Cowper (11), Lyte (10).

**Entity pages updated** with `## Hymnological Context (Duffield)` sections: John Newton, Augustus Toplady, Charles Wesley, Henry Francis Lyte, Reginald Heber, Horatius Bonar, James Montgomery, Frances Ridley Havergal, Charlotte Elliott, Isaac Watts, William Cowper, Martin Luther.

**New entity pages created:** `Edward_Caswall.md` (Oratorian priest; 12 hymns; translator of Bernard's "Jesu dulcis memoria"); `Christopher_Wordsworth.md` (Bishop of Lincoln; The Holy Year 1862).

**Source summary page updated:** `wiki/sources/English_Hymns_Their_Authors_and_History.md`.

## 2026-04-05 | update | Entity pages updated with Duffield context (batch 2)

Added `## Hymnological Context (Duffield)` sections to five additional entity pages with significant Duffield coverage:
- [[Thomas_Kelly]] (25 Duffield entries) — conversion story, Lord Plunket anecdote, late-life testimonial
- [[Philip_Doddridge]] (29 Duffield entries) — morning hymn ritual, Jacob's Vow sermon origin, textual history
- [[Anna_Steele]] (20 Duffield entries) — Duffield's ranking of her as 4th-5th in English hymnody, textual notes
- [[John_Mason_Neale]] (25 Duffield entries) — translation sources, Athens Easter midnight account, publication history
- [[Frederick_William_Faber]] (10 Duffield entries) — Huguenot ancestry, biographical sketch, poetic peak assessment

All five pages updated: source_refs, updated date, new section.

## 2026-04-05 | ingest | The Hymns and Hymn Writers of the Church (Nutter & Tillett, 1911)

Ingested Charles S. Nutter and Wilbur F. Tillett, *The Hymns and Hymn Writers of the Church* (1911), from `raw/Nutter.txt` (90,912 lines, OCR scan). Two index sections processed: Biographical Index of Authors (lines ~55,678-65,083) and Biographical Index of Composers of Tunes (lines ~65,087-67,625). OCR corruption was heavy throughout, particularly in Gothic typeface name headers; many entries located via hymn first-line text rather than author name.

**Data file created:** `wiki/_nutter_composer_data.json` — ~130 composer entries from the full Composers index, with names, dates, nationalities, tune lists, and biographical descriptions. Notable entries: Lowell Mason (34 tunes), Barnby (32 tunes + 3 chants), Lutkin (19 tunes), Dykes (~18 tunes), Sullivan (13 tunes), Stainer (10 tunes).

**New entity pages created (19 total, wiki/entities/):**
- `Mary_Artemisia_Lathbury.md` — (1841-1913) Methodist; Chautauqua; "Break thou the bread of life," "Day is dying in the west"
- `William_Walsham_How.md` — (1823-1897) Church of England bishop; "For all the saints"; 6 hymns in Methodist Hymnal
- `Washington_Gladden.md` — (1836-1918) Congregationalist; social reformer; Williams College 1859; "O Master, let me walk with thee"
- `Frederick_Lucian_Hosmer.md` — (1840-1929) Unitarian; Harvard; Berkeley CA; co-editor Unity Hymns 1880
- `Godfrey_Thring.md` — (1823-1903) Anglican; Prebendary of Wells; Church of England Hymn Book (1880)
- `Matthew_Bridges.md` — (1800-1894) Tractarian convert to Rome; died Quebec; "Crown him with many crowns"
- `Adelaide_Anne_Procter.md` — (1825-1864) English; daughter of "Barry Cornwall"; Roman Catholic convert; Legends and Lyrics (1858)
- `Frank_Mason_North.md` — (1850-1935) Methodist Episcopal; NY City Church Extension; "Where cross the crowded ways of life"
- `Samuel_Longfellow.md` — (1819-1892) Unitarian; brother of Henry Wadsworth Longfellow; Harvard; co-edited A Book of Hymns (1846)
- `William_McDonald.md` — (1820-1901) Methodist Episcopal; National Holiness Association; Salvation Melodies (1874)
- `Karl_Pomeroy_Harrington.md` — (1861-1953) Latin professor Wesleyan University; music editor 1905 Methodist Hymnal; 13 tunes
- `Peter_Christian_Lutkin.md` — (1858-1931) Dean Northwestern University School of Music; music editor 1905 Methodist Hymnal; 19 tunes; "The Lord Bless You and Keep You"
- `Joseph_Perry_Holbrook.md` — (1822-1888) Boston-area composer; Songs of the Sanctuary; Methodist Hymnal 1878 editor with Tourjee; tunes Truman and Greek Hymn
- `Joseph_Anstice.md` — (1808-1836) Oxford; Professor of Classical Literature King's College London; dictated 52 hymns to wife during final illness; died age 28
- `Elizabeth_Payson_Prentiss.md` — (1818-1878) Born Portland ME; daughter of Edward Payson; Stepping Heavenward (1869); "More love to thee, O Christ"
- `John_Hart_Stockton.md` — (1813-1877) Methodist Episcopal; Salvation Melodies (1874); "Come, every soul by sin oppressed"; tune Invodale
- `Henry_Williams_Baker.md` — (1821-1877) Anglican; Trinity College Cambridge; vicar Monkland; editor-in-chief Hymns Ancient and Modern; died quoting his own "The King of love my Shepherd is"
- `William_Chatterton_Dix.md` — (1837-1898) Born Bristol; marine insurance manager Glasgow; "As with gladness men of old," "Alleluia! sing to Jesus"
- `William_Fisk_Sherwin.md` — (1826-1887) American composer; Chautauqua music director; tunes "Evening Praise" and "Bread of Life" for Lathbury's texts; Nutter: "few tunes in this Hymnal are more admired"

**Existing entity pages updated** with `## Methodist Hymnal Context (Nutter)` sections:
- `Lowell_Mason.md` — Nutter's assessment as greatest contributor to American church music; 34 tunes in 1905 Methodist Hymnal; Missionary Hymn story; public schools contribution; George James Webb link
- `Robert_Lowry.md` — Nutter describes him as "well-known American Baptist minister" for whom "music was his avocation"; 3 tunes in the Hymnal (Something for Jesus, One More Day's Work, I Need Thee Every Hour)

**Index updated:** 1,607 pages total (19 new entity pages + 1 JSON data file); all 19 new entity names added to Entities section of `_index.md`.

## 2026-04-05 | enrich | Hymn Page Enrichment Script

Ran `factory/scripts/enrich_hymns.py` to push extracted data from Duffield, Metcalf, and Nutter into the 1,324 hymn stub pages.

**Data sources used:**
- `_duffield_hymn_data.json` — 1,081 hymn entries (matched 419 to Campbell hymns)
- `_metcalf_tune_data.json` — 54 tune-to-hymn pairings (matched 24)
- `_nutter_hymn_data_part1.json` + `_nutter_hymn_data_part2.json` — 832 hymn annotations (matched 265)
- `_nutter_composer_data.json` — 189 composer entries with 433 tune mappings

**Results:**
- 500 hymn pages upgraded from `status: stub` to `status: draft`
- 505 hymn pages received `era` values (previously empty)
- 29 hymn pages received `composer` values (previously empty)
- 26 hymn pages received `tune_name` values (previously empty)
- 486 hymn pages received real Historical Context sections (replacing placeholders)
- 419 hymn pages received Duffield source attribution
- 265 hymn pages received Nutter source attribution
- 24 hymn pages received Metcalf source attribution

**Remaining gaps:**
- 824 hymns still `status: stub` (no matching data in the 5 new sources)
- 819 hymns still lack era values (minor/anonymous authors not in era lookup table)
- 1,295 hymns still lack composer information (tune data sparse for Campbell's 1870 collection)

## 2026-04-05 | enrich | Portrait Images Added to Entity Pages

Added public domain portrait images from Wikimedia Commons to 20 entity pages and 3 concept pages. All images verified CC0 or public domain.

**Tier 1 entity portraits (all 10 added):**
- [[Isaac_Watts]] — NPG portrait
- [[Charles_Wesley]] — classic portrait
- [[John_Newton]] — National Library of Wales portrait
- [[Martin_Luther]] — Cranach the Elder (Statens Museum, CC0)
- [[Fanny_Crosby]] — portrait photograph
- [[Augustus_Toplady]] — engraved portrait
- [[William_Cowper]] — Lemuel Francis Abbott, 1792
- [[Reginald_Heber]] — formal portrait
- [[Charlotte_Elliott]] — portrait with signature
- [[Philip_Doddridge]] — engraved portrait

**Tier 2 entity portraits (10 added):**
- [[John_Henry_Newman]], [[John_Keble]], [[Frances_Ridley_Havergal]], [[Paul_Gerhardt]], [[Lowell_Mason]], [[Thomas_Hastings]], [[George_Frederic_Handel]] (Denner portrait), [[John_Mason_Neale]], [[Phillips_Brooks]]
- Note: Paul Gerhardt image confirmed by Wikidata structured data

**Historical scene images (3 added to concept pages):**
- [[Reformation_Hymnody]] — Ferdinand Pauwels, "Luther Hammers His 95 Theses" (public domain)
- [[Camp_Meeting_Hymns]] — Methodist Camp Meeting, 1819 engraving (public domain)
- [[Revival_Hymns]] — J. Maze Burbank, "Religious Camp Meeting," 1839 watercolor (public domain)

## 2026-04-05 | summary | Five-Source Ingest Complete

Ingested 5 new sources totaling 216,756 lines of OCR text into the Hymn Wiki:

| Source | Author | Year | Lines | New Entities | Updated Entities | New Concepts | Updated Concepts |
|--------|--------|------|-------|-------------|-----------------|-------------|-----------------|
| The English Hymn | Benson | 1915 | 34,910 | 5 | 2 | 7 | 7 |
| Baptist Hymn Writers | Burrage | 1888 | 36,616 | ~17 | ~16 | 2 | 0 |
| English Hymns: Authors & History | Duffield | 1886 | 38,337 | 2 | ~15 | 0 | 0 |
| American Sacred Music Writers | Metcalf | 1925 | 15,981 | 26 | 11 | 0 | 0 |
| Hymns & Hymn Writers of the Church | Nutter | 1911 | 90,912 | 19 | 2 | 0 | 0 |
| **Totals** | | | **216,756** | **~69** | **~46** | **9** | **7** |

**Wiki totals after ingest:** 227 entities, 39 concepts, 9 sources, 5 synthesis, 1 timeline, 1,324 hymns. Total pages: ~1,616.

**Hymn page enrichment:** 500 of 1,324 hymn pages upgraded from stub to draft. 486 received historical context. 505 received era assignments. 29 received composer data.

## 2026-04-05 | enrich | Famous Hymns Historical Context

Web-researched and enriched 14 of the most famous hymns with full Historical Context sections. For each hymn: replaced thin/fragmented source notes with 200–450 word narratives covering composition story, writer's life context, cultural impact, textual history, and tune information. Also filled in missing `composer`, `tune_name`, and `era` frontmatter fields. Updated `source_refs` to include `[[Web_Research]]`.

**Hymns enriched:**

| File | Title | Author | Key Story |
|------|-------|--------|-----------|
| Hymn_0403 | Amazing Grace | John Newton | Slave trade → storm conversion → Olney Hymns; "ten thousand years" stanza's African-American origin |
| Hymn_0261 | Rock of Ages | Augustus Toplady | Gospel Magazine 1776; Burrington Combe legend debunked; Toplady-Wesley feud |
| Hymn_1227 | Abide With Me | Henry Francis Lyte | Final sermon, Sept 4 1847, dying of TB; Monk's tune composed in grief at sunset |
| Hymn_0343 | Just As I Am | Charlotte Elliott | 1834 invalid, César Malan's counsel, Billy Graham altar calls |
| Hymn_0262 | Jesus Lover of My Soul | Charles Wesley | 1740, hawk-and-bird legend; John Wesley's reluctance to publish it |
| Hymn_0512 | When I Survey the Wondrous Cross | Isaac Watts | 1707, first English first-person hymn; Charles Wesley's tribute |
| Hymn_0928 | Nearer My God to Thee | Sarah Flower Adams | 1841; McKinley deathbed; Titanic controversy |
| Hymn_0495 | Blest Be the Tie That Binds | John Fawcett | 1782 Wainsgate; refused London call; wagon-unloading story |
| Hymn_0542 | My Faith Looks Up to Thee | Ray Palmer | 1830 pocket-book poem; Mason street encounter; tune Olivet composed same evening |
| Hymn_0792 | How Firm a Foundation | "K" (George Keith?) | 1787 Rippon's Selection; anonymous mystery; Andrew Jackson, Robert E. Lee, Theodore Roosevelt connections |
| Hymn_0125 | Joy to the World | Isaac Watts | 1719 Psalm 98 paraphrase; NOT originally a Christmas hymn; Lowell Mason's "Antioch" tune |
| Hymn_0590 | Lead Kindly Light | John Henry Newman | 1833 Mediterranean becalming; Oxford Movement; Newman's 2019 canonization |
| Hymn_0660 | Come Thou Fount / O Thou Fount | Robert Robinson | 1758 at age 22; "prone to wander" autobiography; later drift and the famous coach story |
| Hymn_0075 | O God Our Help in Ages Past | Isaac Watts | 1714 written during Queen Anne's succession crisis; Wesley's line change; British near-national-anthem status |

**Hymns not found in this collection:** "O for a Thousand Tongues" (Wesley), "Holy Holy Holy" (Heber), "All Hail the Power of Jesus' Name" (Perronet), "Onward Christian Soldiers" (Baring-Gould) — these titles/authors do not appear to be in the 1870 Campbell collection used as source.

**Note:** Hymn_0177 (O Sacred Head Now Wounded) was already fully enriched from a prior session; no changes needed.

## [2026-04-05] edit | YouTube Listen Sections Added

Added `## Listen` sections with YouTube performance links to 10 hymn pages (the most well-known hymns present in the 1870 Campbell collection). Video IDs sourced via web search and page fetching.

| Hymn | Title | YouTube Link Description |
|------|-------|--------------------------|
| Hymn_0403 | Amazing Grace | Tabernacle Choir, Mack Wilberg orchestral arrangement |
| Hymn_0261 | Rock of Ages | Antrim Mennonite Choir, unaccompanied four-part |
| Hymn_1227 | Abide With Me | Tabernacle Choir, tune Eventide (Monk) |
| Hymn_0512 | When I Survey the Wondrous Cross | Tabernacle Choir, Hamburg tune (Lowell Mason) |
| Hymn_0660 | Come Thou Fount / O Thou Fount | Traditional congregational arrangement, tune Nettleton |
| Hymn_0262 | Jesus, Lover of My Soul | Welsh Male Voice Choir, Aberystwyth tune (Joseph Parry) |
| Hymn_0928 | Nearer, My God, to Thee | Anna Richey solo, tune Bethany (Lowell Mason) |
| Hymn_0590 | Shed Kindly Light / Lead Kindly Light | Choral, tune Lux Benigna (John Bacchus Dykes) |
| Hymn_0125 | Joy to the World | Tabernacle Choir, orchestral, tune Antioch (Lowell Mason) |
| Hymn_0075 | Our God, Our Help in Ages Past | Westminster Abbey, tune St Anne (William Croft) |

**Three hymns not updated** (YouTube video IDs could not be confirmed): Hymn_0343 (Just As I Am), Hymn_0495 (Blest Be the Tie That Binds), Hymn_0542 (My Faith Looks Up to Thee).

## [2026-04-05] edit | YouTube Listen Sections — Second Pass

Added `## Listen` sections to 2 more hymn pages after additional web research:

| Hymn | Title | YouTube Link Description |
|------|-------|--------------------------|
| Hymn_0343 | Just As I Am | HymnCharts lyrics/sing-along video, tune Woodworth (William Bradbury) |
| Hymn_0495 | Blest Be the Tie That Binds | Sara Groves retuned version, *The Collection* (2013), tune Dennis |

**One hymn still without a Listen section:** Hymn_0542 (My Faith Looks Up to Thee, Ray Palmer) — no confirmed YouTube video ID found after extensive searching.

## 2026-04-05 | fix | Structural fixes and content polish

**Overview page (`_overview.md`) updated:**
- Sources section expanded from 4 to 9 sources with full listing
- Browse by Tradition sections merged (removed duplicate "continued" section)
- Browse by Type now includes Sources and explicit page counts
- Featured section now includes Hymns with Recordings and Random Hymn

**New pages created:**
- `Sources_Overview.md` — navigation page for all 9 source pages (fixes broken breadcrumbs)
- `Hymns_with_Recordings.md` — navigation page for 12 hymns with YouTube performance links
- `Random_Hymn.md` — discovery page with sampling links across the collection

**YouTube links:** Updated all 12 hymn pages to open YouTube links in new windows (`target="_blank"`).

**Index rebuilt.** Total pages: ~1,616.

## 2026-04-05 | maintenance | YouTube Link Verification

Verified all 12 hymn YouTube links via YouTube oEmbed API. Found 2 broken links and replaced them with working alternatives.

**Verified working (10 hymns):**
- Hymn_0075 (O God Our Help) — `rsHIwXTjAOU` — Westminster Abbey, "Oh God Our Help in Ages Past"
- Hymn_0261 (Rock of Ages) — `gM7gt_cSxjw` — SE Samonte, "Rock of Ages"
- Hymn_0262 (Jesus Lover of My Soul) — `moMR1dCwx8M` — Treorchy Male Voice Choir, "Aberystwyth"
- Hymn_0343 (Just As I Am) — `1Ia_YK6reTc` — Hymncharts, "Just As I Am [Lyrics Video]"
- Hymn_0403 (Amazing Grace) — `C2arm5ydeJc` — The Tabernacle Choir, "Amazing Grace"
- Hymn_0495 (Blest Be the Tie) — `gcYFtihSg_8` — SaraGrovesVEVO, "Blessed Be the Tie"
- Hymn_0512 (When I Survey the Wondrous Cross) — `SsBiaBTFADI` — The Tabernacle Choir
- Hymn_0660 (O Thou Fount of Every Blessing) — `iGmK9tR9lbQ` — Jeremiah Wesley, "Come Thou Fount"
- Hymn_0928 (Nearer My God to Thee) — `UAgm0AtPQ-g` — Anna Richey live cover
- Hymn_1227 (Abide With Me) — `YvZsOTJEUUc` — The Tabernacle Choir

**Replaced (2 hymns):**
- Hymn_0125 (Joy to the World) — `7r3vvMUHAXU` → `dJ87_7iLsj0` — Gardiner Sisters, "#LightTheWorld"
- Hymn_0590 (Lead Kindly Light) — `cvIJkteSnXQ` → `YzpHUty5rjs` — General Conference of The Church of Jesus Christ

## [2026-04-05] maintenance | Dead Author Wikilink Resolution

Resolved all dead author wikilinks in 1,324 hymn pages. Found ~290 unique dead link types affecting 413 hymn files total.
- **Redirected** 32 abbreviated/variant author names to existing entity pages (e.g., [[Hastings]] -> [[Thomas Hastings]], [[Anne Steele]] -> [[Anna Steele]])
- **Removed wikilinks** from ~190 collection references and unidentifiable abbreviations (e.g., Wardlaw's Coll, Ancient Hymns, Psalmist)
- **Created 55 new entity stubs** for identifiable authors who lacked pages (e.g., Josiah Conder, James Edmeston, John Wesley, Felicia Hemans)
- Entity count: 227 -> 282
