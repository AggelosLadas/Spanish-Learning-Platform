"""
Seed data for chapters 11-15 (intermediate level).
Run: python -m app.db.seed_chapters_11_15
"""
from app.db.database import SessionLocal, engine, Base
from app.models.chapter import Chapter
from app.models.section import Section
from app.models.question import Question
from app.models.exam import Exam


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Chapter).filter(Chapter.order_index == 11).first():
        print("Chapter 11 already exists. Skipping seed for chapters 11-15.")
        db.close()
        return

    chapters_data = [
        # ──────────────────────────────────────────────
        # CHAPTER 11 — Irregular Verbs: ir, tener, hacer
        # ──────────────────────────────────────────────
        {
            "order_index": 11,
            "title_greek": "Ανώμαλα Ρήματα (ir, tener, hacer)",
            "title_spanish": "Verbos Irregulares (ir, tener, hacer)",
            "difficulty_level": "intermediate",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή στα Ανώμαλα Ρήματα",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις τρία από τα πιο σημαντικά ανώμαλα ρήματα στα Ισπανικά: ir (πηγαίνω), tener (έχω) και hacer (κάνω). Αυτά τα ρήματα δεν ακολουθούν τους κανονικούς κανόνες κλίσης και χρησιμοποιούνται πολύ συχνά στην καθημερινή ομιλία.",
                    },
                },
                {
                    "order_index": 2,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση του IR (πηγαίνω)",
                        "body": "Το ρήμα IR είναι εντελώς ανώμαλο. Χρησιμοποιείται επίσης για να σχηματίσουμε τον κοντινό μέλλοντα: ir + a + απαρέμφατο.",
                        "rules": [
                            "Yo voy → Εγώ πηγαίνω",
                            "Tú vas → Εσύ πηγαίνεις",
                            "Él/Ella va → Αυτός/Αυτή πηγαίνει",
                            "Nosotros vamos → Εμείς πηγαίνουμε",
                            "Vosotros vais → Εσείς πηγαίνετε",
                            "Ellos/Ellas van → Αυτοί/Αυτές πηγαίνουν",
                            "IR + A + απαρέμφατο = κοντινός μέλλοντας: Voy a comer → Θα φάω",
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση του TENER (έχω) & Εκφράσεις",
                        "body": "Το TENER είναι ανώμαλο και χρησιμοποιείται σε πολλές καθημερινές εκφράσεις που στα Ελληνικά χρησιμοποιούν το «είμαι».",
                        "rules": [
                            "Yo tengo → Εγώ έχω",
                            "Tú tienes → Εσύ έχεις",
                            "Él/Ella tiene → Αυτός/Αυτή έχει",
                            "Nosotros tenemos → Εμείς έχουμε",
                            "Vosotros tenéis → Εσείς έχετε",
                            "Ellos/Ellas tienen → Αυτοί/Αυτές έχουν",
                            "Tener hambre → Πεινάω (κυριολ. «έχω πείνα»)",
                            "Tener sed → Διψάω (κυριολ. «έχω δίψα»)",
                            "Tener frío → Κρυώνω (κυριολ. «έχω κρύο»)",
                            "Tener calor → Ζεσταίνομαι (κυριολ. «έχω ζέστη»)",
                            "Tener sueño → Νυστάζω (κυριολ. «έχω ύπνο»)",
                            "Tener miedo → Φοβάμαι (κυριολ. «έχω φόβο»)",
                            "Tener que + απαρέμφατο → Πρέπει να: Tengo que estudiar → Πρέπει να διαβάσω",
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση του HACER (κάνω)",
                        "body": "Το HACER χρησιμοποιείται για δραστηριότητες, τον καιρό και πολλές εκφράσεις.",
                        "rules": [
                            "Yo hago → Εγώ κάνω",
                            "Tú haces → Εσύ κάνεις",
                            "Él/Ella hace → Αυτός/Αυτή κάνει",
                            "Nosotros hacemos → Εμείς κάνουμε",
                            "Vosotros hacéis → Εσείς κάνετε",
                            "Ellos/Ellas hacen → Αυτοί/Αυτές κάνουν",
                            "Hacer calor → Κάνει ζέστη",
                            "Hacer frío → Κάνει κρύο",
                            "Hacer ejercicio → Κάνω γυμναστική",
                            "Hacer la tarea → Κάνω τα μαθήματά μου",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα σε Πλαίσιο",
                        "examples": [
                            {"spanish": "— ¿Adónde vas?\n— Voy al supermercado.", "greek": "— Πού πηγαίνεις;\n— Πηγαίνω στο σούπερ μάρκετ."},
                            {"spanish": "— ¿Tienes hambre?\n— Sí, tengo mucha hambre.", "greek": "— Πεινάς;\n— Ναι, πεινάω πολύ."},
                            {"spanish": "— ¿Qué haces hoy?\n— Hago ejercicio y después voy a estudiar.", "greek": "— Τι κάνεις σήμερα;\n— Κάνω γυμναστική και μετά θα διαβάσω."},
                            {"spanish": "Mañana vamos a ir a la playa.", "greek": "Αύριο θα πάμε στην παραλία."},
                            {"spanish": "Ella tiene que trabajar mañana.", "greek": "Αυτή πρέπει να δουλέψει αύριο."},
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Χρήσιμες Συμβουλές",
                        "tips": [
                            "Στα Ισπανικά λέμε «tengo hambre» (έχω πείνα) αντί για «είμαι πεινασμένος» — θυμήσου ότι το tener αντικαθιστά το «είμαι» σε πολλές εκφράσεις!",
                            "Το «ir + a + απαρέμφατο» είναι ο ευκολότερος τρόπος να μιλήσεις για το μέλλον. Αντιστοιχεί στο «θα» στα Ελληνικά.",
                            "Το hacer χρησιμοποιείται για τον καιρό: Hace calor = Κάνει ζέστη. Δεν χρειάζεται υποκείμενο!",
                            "Μάθε πρώτα τα τρία αυτά ρήματα πολύ καλά — εμφανίζονται σχεδόν σε κάθε συζήτηση!",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Ποια είναι η σωστή κλίση; «Εγώ πηγαίνω» =", "options_json": ["Yo vas", "Yo voy", "Yo va", "Yo ir"], "correct_answer": "Yo voy", "explanation": "Voy = πηγαίνω (1ο πρόσ. του ir)", "points": 1},
                {"type": "fill_blank", "prompt": "Tú _____ dos hermanos. (Εσύ έχεις δύο αδέρφια)", "options_json": None, "correct_answer": "tienes", "explanation": "Tienes = έχεις (2ο πρόσ. του tener)", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Αυτός κάνει» στα Ισπανικά;", "options_json": ["Él hago", "Él haces", "Él hace", "Él hacen"], "correct_answer": "Él hace", "explanation": "Hace = κάνει (3ο πρόσ. του hacer)", "points": 1},
                {"type": "true_false", "prompt": "Η έκφραση «tengo hambre» σημαίνει «έχω πείνα» (πεινάω).", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Tener hambre = πεινάω (κυριολ. έχω πείνα)", "points": 1},
                {"type": "fill_blank", "prompt": "Nosotros _____ al parque. (Εμείς πηγαίνουμε στο πάρκο)", "options_json": None, "correct_answer": "vamos", "explanation": "Vamos = πηγαίνουμε (1ο πληθ. του ir)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Κάνει κρύο»", "options_json": None, "correct_answer": "Hace frío", "explanation": "Hacer + frío = κάνει κρύο (για τον καιρό)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «Voy a comer»;", "options_json": ["Πηγαίνω να φάω", "Θα φάω", "Τρώω τώρα", "Έφαγα"], "correct_answer": "Θα φάω", "explanation": "Ir + a + απαρέμφατο = κοντινός μέλλοντας", "points": 1},
                {"type": "fill_blank", "prompt": "Ellos _____ ejercicio todos los días. (Αυτοί κάνουν γυμναστική κάθε μέρα)", "options_json": None, "correct_answer": "hacen", "explanation": "Hacen = κάνουν (3ο πληθ. του hacer)", "points": 1},
                {"type": "true_false", "prompt": "Η φράση «tener que + απαρέμφατο» σημαίνει «πρέπει να».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Tengo que estudiar = Πρέπει να διαβάσω", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια πρόταση είναι σωστή;", "options_json": ["Yo tengo sueño", "Yo soy sueño", "Yo estoy sueño", "Yo hago sueño"], "correct_answer": "Yo tengo sueño", "explanation": "Tener sueño = νυστάζω", "points": 1},
                {"type": "fill_blank", "prompt": "¿Adónde _____ tú? (Πού πηγαίνεις;)", "options_json": None, "correct_answer": "vas", "explanation": "Vas = πηγαίνεις (2ο πρόσ. του ir)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Πρέπει να δουλέψω»", "options_json": None, "correct_answer": "Tengo que trabajar", "explanation": "Tener que + απαρέμφατο = πρέπει να", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «Ella tiene miedo»;", "options_json": ["Αυτή έχει φίλους", "Αυτή φοβάται", "Αυτή κρυώνει", "Αυτή πεινάει"], "correct_answer": "Αυτή φοβάται", "explanation": "Tener miedo = φοβάμαι", "points": 1},
                {"type": "true_false", "prompt": "Το ρήμα «ir» ακολουθεί κανονική κλίση σε -ir.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Το ir είναι εντελώς ανώμαλο: voy, vas, va, vamos, vais, van", "points": 1},
                {"type": "fill_blank", "prompt": "Yo _____ la tarea por la tarde. (Κάνω τα μαθήματά μου το απόγευμα)", "options_json": None, "correct_answer": "hago", "explanation": "Hago = κάνω (1ο πρόσ. του hacer)", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Ανώμαλα Ρήματα", "passing_score_pct": 60},
        },
        # ──────────────────────────────────────────────
        # CHAPTER 12 — Numbers 20-1000 & Prices
        # ──────────────────────────────────────────────
        {
            "order_index": 12,
            "title_greek": "Αριθμοί 20-1000 & Τιμές",
            "title_spanish": "Números 20-1000 y Precios",
            "difficulty_level": "intermediate",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή στους Μεγάλους Αριθμούς και τις Αγορές",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις τους αριθμούς από το 20 μέχρι το 1000, πώς να ρωτάς και να λες τιμές, και βασικό λεξιλόγιο για ψώνια. Θα μπορείς να ψωνίζεις στα Ισπανικά!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Αριθμοί 20-100",
                        "words": [
                            {"greek": "20", "spanish": "Veinte", "pronunciation": "Βέιντε"},
                            {"greek": "21", "spanish": "Veintiuno", "pronunciation": "Βεϊντιούνο"},
                            {"greek": "22", "spanish": "Veintidós", "pronunciation": "Βεϊντιντός"},
                            {"greek": "30", "spanish": "Treinta", "pronunciation": "Τρέιντα"},
                            {"greek": "31", "spanish": "Treinta y uno", "pronunciation": "Τρέιντα ι ούνο"},
                            {"greek": "40", "spanish": "Cuarenta", "pronunciation": "Κουαρέντα"},
                            {"greek": "50", "spanish": "Cincuenta", "pronunciation": "Θινκουέντα"},
                            {"greek": "60", "spanish": "Sesenta", "pronunciation": "Σεσέντα"},
                            {"greek": "70", "spanish": "Setenta", "pronunciation": "Σετέντα"},
                            {"greek": "80", "spanish": "Ochenta", "pronunciation": "Οτσέντα"},
                            {"greek": "90", "spanish": "Noventa", "pronunciation": "Νοβέντα"},
                            {"greek": "100", "spanish": "Cien", "pronunciation": "Θιέν"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Αριθμοί 100-1000",
                        "words": [
                            {"greek": "100", "spanish": "Cien", "pronunciation": "Θιέν"},
                            {"greek": "101", "spanish": "Ciento uno", "pronunciation": "Θιέντο ούνο"},
                            {"greek": "200", "spanish": "Doscientos", "pronunciation": "Ντοσθιέντος"},
                            {"greek": "300", "spanish": "Trescientos", "pronunciation": "Τρεσθιέντος"},
                            {"greek": "400", "spanish": "Cuatrocientos", "pronunciation": "Κουατροθιέντος"},
                            {"greek": "500", "spanish": "Quinientos", "pronunciation": "Κινιέντος"},
                            {"greek": "600", "spanish": "Seiscientos", "pronunciation": "Σεϊσθιέντος"},
                            {"greek": "700", "spanish": "Setecientos", "pronunciation": "Σετεθιέντος"},
                            {"greek": "800", "spanish": "Ochocientos", "pronunciation": "Οτσοθιέντος"},
                            {"greek": "900", "spanish": "Novecientos", "pronunciation": "Νοβεθιέντος"},
                            {"greek": "1000", "spanish": "Mil", "pronunciation": "Μιλ"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Εκφράσεις για Αγορές",
                        "body": "Μάθε τις βασικές φράσεις που χρειάζεσαι για να ψωνίσεις στα Ισπανικά.",
                        "rules": [
                            "¿Cuánto cuesta? → Πόσο κοστίζει;",
                            "¿Cuánto cuestan? → Πόσο κοστίζουν; (πληθυντικός)",
                            "Cuesta diez euros. → Κοστίζει δέκα ευρώ.",
                            "Cuestan veinte euros. → Κοστίζουν είκοσι ευρώ.",
                            "¿Tiene algo más barato? → Έχετε κάτι πιο φτηνό;",
                            "Es muy caro. → Είναι πολύ ακριβό.",
                            "Es barato. → Είναι φτηνό.",
                            "Me lo llevo. → Θα το πάρω.",
                            "¿Puedo pagar con tarjeta? → Μπορώ να πληρώσω με κάρτα;",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Διάλογοι στο Κατάστημα",
                        "examples": [
                            {
                                "spanish": "— ¡Buenos días! ¿Cuánto cuesta esta camiseta?\n— Cuesta veinticinco euros.\n— ¿Tiene algo más barato?\n— Sí, esta cuesta quince euros.\n— Me la llevo, gracias.",
                                "greek": "— Καλημέρα! Πόσο κοστίζει αυτό το μπλουζάκι;\n— Κοστίζει είκοσι πέντε ευρώ.\n— Έχετε κάτι πιο φτηνό;\n— Ναι, αυτό κοστίζει δεκαπέντε ευρώ.\n— Θα το πάρω, ευχαριστώ.",
                            },
                            {
                                "spanish": "— ¿Cuánto cuestan estos zapatos?\n— Cuestan ochenta y cinco euros.\n— ¡Es muy caro! ¿Puedo pagar con tarjeta?\n— Sí, por supuesto.",
                                "greek": "— Πόσο κοστίζουν αυτά τα παπούτσια;\n— Κοστίζουν ογδόντα πέντε ευρώ.\n— Είναι πολύ ακριβό! Μπορώ να πληρώσω με κάρτα;\n— Ναι, φυσικά.",
                            },
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Συμβουλές για τους Αριθμούς",
                        "tips": [
                            "Οι αριθμοί 21-29 γράφονται σε μία λέξη: veintiuno, veintidós, veintitrés...",
                            "Από το 30 και πάνω χωρίζονται: treinta y uno, treinta y dos...",
                            "Cien = ακριβώς 100. Για 101-199 χρησιμοποιούμε ciento: ciento uno, ciento dos...",
                            "Τα εκατοντάδες 200-900 αλλάζουν γένος: doscientos (αρσ.) / doscientas (θηλ.)",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «50» στα Ισπανικά;", "options_json": ["Cuarenta", "Cincuenta", "Sesenta", "Setenta"], "correct_answer": "Cincuenta", "explanation": "50 = Cincuenta", "points": 1},
                {"type": "fill_blank", "prompt": "Πώς λέμε «30» στα Ισπανικά; _____", "options_json": None, "correct_answer": "treinta", "explanation": "30 = treinta", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «¿Cuánto cuesta?»;", "options_json": ["Πού είναι;", "Πόσο κοστίζει;", "Τι ώρα είναι;", "Πώς σε λένε;"], "correct_answer": "Πόσο κοστίζει;", "explanation": "¿Cuánto cuesta? = Πόσο κοστίζει;", "points": 1},
                {"type": "true_false", "prompt": "Ο αριθμός «veinticinco» σημαίνει 35.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Veinticinco = 25, όχι 35", "points": 1},
                {"type": "fill_blank", "prompt": "¿Cuánto _____ estos zapatos? (Πόσο κοστίζουν αυτά τα παπούτσια;)", "options_json": None, "correct_answer": "cuestan", "explanation": "Cuestan = κοστίζουν (πληθυντικός)", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «1000» στα Ισπανικά;", "options_json": ["Cien", "Ciento", "Mil", "Millón"], "correct_answer": "Mil", "explanation": "1000 = Mil", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Είναι πολύ ακριβό»", "options_json": None, "correct_answer": "Es muy caro", "explanation": "Es muy caro = Είναι πολύ ακριβό", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «100» ακριβώς;", "options_json": ["Ciento", "Cien", "Cent", "Cientos"], "correct_answer": "Cien", "explanation": "Cien = ακριβώς 100. Ciento χρησιμοποιείται σε 101-199.", "points": 1},
                {"type": "true_false", "prompt": "Οι αριθμοί 21-29 γράφονται σε μία λέξη στα Ισπανικά.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "21-29: veintiuno, veintidós, veintitrés κ.λπ.", "points": 1},
                {"type": "fill_blank", "prompt": "Cuesta _____ euros. (Κοστίζει 45 ευρώ)", "options_json": None, "correct_answer": "cuarenta y cinco", "explanation": "45 = cuarenta y cinco", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Αριθμοί 20-1000 & Τιμές", "passing_score_pct": 60},
        },
        # ──────────────────────────────────────────────
        # CHAPTER 13 — Past Tense: Pretérito Indefinido
        # ──────────────────────────────────────────────
        {
            "order_index": 13,
            "title_greek": "Χρόνος Παρελθόντος: Pretérito Indefinido",
            "title_spanish": "Pretérito Indefinido",
            "difficulty_level": "intermediate",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή στον Αόριστο (Pretérito Indefinido)",
                        "body": "Ο Pretérito Indefinido είναι ο βασικός χρόνος παρελθόντος στα Ισπανικά. Χρησιμοποιείται για ενέργειες που ολοκληρώθηκαν σε συγκεκριμένο χρόνο στο παρελθόν. Σε αυτό το κεφάλαιο θα μάθεις την κλίση των κανονικών ρημάτων σε -AR, -ER και -IR.",
                    },
                },
                {
                    "order_index": 2,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση Ρημάτων σε -AR (Αόριστος)",
                        "body": "Παράδειγμα: HABLAR (μιλάω) → Αόριστος",
                        "rules": [
                            "Yo hablé → Εγώ μίλησα",
                            "Tú hablaste → Εσύ μίλησες",
                            "Él/Ella habló → Αυτός/Αυτή μίλησε",
                            "Nosotros hablamos → Εμείς μιλήσαμε",
                            "Vosotros hablasteis → Εσείς μιλήσατε",
                            "Ellos/Ellas hablaron → Αυτοί/Αυτές μίλησαν",
                            "Καταλήξεις -AR: -é, -aste, -ó, -amos, -asteis, -aron",
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση Ρημάτων σε -ER / -IR (Αόριστος)",
                        "body": "Τα ρήματα σε -ER και -IR μοιράζονται τις ίδιες καταλήξεις στον αόριστο. Παράδειγμα: COMER (τρώω) / VIVIR (ζω)",
                        "rules": [
                            "Yo comí / viví → Εγώ έφαγα / έζησα",
                            "Tú comiste / viviste → Εσύ έφαγες / έζησες",
                            "Él/Ella comió / vivió → Αυτός/Αυτή έφαγε / έζησε",
                            "Nosotros comimos / vivimos → Εμείς φάγαμε / ζήσαμε",
                            "Vosotros comisteis / vivisteis → Εσείς φάγατε / ζήσατε",
                            "Ellos/Ellas comieron / vivieron → Αυτοί/Αυτές έφαγαν / έζησαν",
                            "Καταλήξεις -ER/-IR: -í, -iste, -ió, -imos, -isteis, -ieron",
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "vocab",
                    "content_json": {
                        "title": "Χρονικές Εκφράσεις Παρελθόντος",
                        "words": [
                            {"greek": "Χθες", "spanish": "Ayer", "pronunciation": "Αγιέρ"},
                            {"greek": "Χθες το βράδυ", "spanish": "Anoche", "pronunciation": "Ανότσε"},
                            {"greek": "Προχθές", "spanish": "Anteayer", "pronunciation": "Αντεαγιέρ"},
                            {"greek": "Την περασμένη εβδομάδα", "spanish": "La semana pasada", "pronunciation": "Λα σεμάνα πασάδα"},
                            {"greek": "Τον περασμένο μήνα", "spanish": "El mes pasado", "pronunciation": "Ελ μες πασάδο"},
                            {"greek": "Πέρσι", "spanish": "El año pasado", "pronunciation": "Ελ άνιο πασάδο"},
                            {"greek": "Πριν δύο μέρες", "spanish": "Hace dos días", "pronunciation": "Άθε ντος ντίας"},
                            {"greek": "Πρόσφατα", "spanish": "Recientemente", "pronunciation": "Ρεθιεντεμέντε"},
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα Χρήσης",
                        "examples": [
                            {"spanish": "Ayer hablé con mi madre por teléfono.", "greek": "Χθες μίλησα με τη μητέρα μου στο τηλέφωνο."},
                            {"spanish": "Anoche comimos en un restaurante italiano.", "greek": "Χθες το βράδυ φάγαμε σε ένα ιταλικό εστιατόριο."},
                            {"spanish": "El año pasado viví en Barcelona.", "greek": "Πέρσι έζησα στη Βαρκελώνη."},
                            {"spanish": "¿Estudiaste para el examen?", "greek": "Διάβασες για τις εξετάσεις;"},
                            {"spanish": "Ellos viajaron a México hace dos años.", "greek": "Αυτοί ταξίδεψαν στο Μεξικό πριν δύο χρόνια."},
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Συμβουλές για τον Αόριστο",
                        "tips": [
                            "Πρόσεξε τους τόνους! Στον αόριστο, η πρώτη και τρίτη σε ενικό έχουν πάντα τόνο: hablé, habló.",
                            "Η 1η πληθυντικού (-amos / -imos) είναι η ίδια στον ενεστώτα και τον αόριστο! Μόνο από τα συμφραζόμενα καταλαβαίνουμε.",
                            "Χρησιμοποίησε πάντα χρονικές εκφράσεις (ayer, anoche κ.λπ.) για να ξεκαθαρίσεις ότι μιλάς για το παρελθόν.",
                            "Ο αόριστος στα Ισπανικά αντιστοιχεί στον Ελληνικό αόριστο: μίλησα, έφαγα, έζησα.",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Ποια είναι η σωστή κλίση; «Εγώ μίλησα» =", "options_json": ["Yo hablo", "Yo hablé", "Yo habló", "Yo hablaste"], "correct_answer": "Yo hablé", "explanation": "Hablé = μίλησα (1ο πρόσ. αόριστος -AR)", "points": 1},
                {"type": "fill_blank", "prompt": "Ayer ella _____ una carta. (Χθες αυτή έγραψε ένα γράμμα) — escribir", "options_json": None, "correct_answer": "escribió", "explanation": "Escribió = έγραψε (3ο πρόσ. αόριστος -IR)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «ayer»;", "options_json": ["Σήμερα", "Αύριο", "Χθες", "Πάντα"], "correct_answer": "Χθες", "explanation": "Ayer = Χθες", "points": 1},
                {"type": "true_false", "prompt": "Τα ρήματα σε -ER και -IR έχουν τις ίδιες καταλήξεις στον αόριστο.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Και τα δύο: -í, -iste, -ió, -imos, -isteis, -ieron", "points": 1},
                {"type": "fill_blank", "prompt": "Nosotros _____ en un restaurante anoche. (Φάγαμε σε εστιατόριο χθες βράδυ) — comer", "options_json": None, "correct_answer": "comimos", "explanation": "Comimos = φάγαμε (1ο πληθ. αόριστος -ER)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Χθες μίλησα με τον φίλο μου»", "options_json": None, "correct_answer": "Ayer hablé con mi amigo", "explanation": "Ayer = χθες, hablé = μίλησα, con mi amigo = με τον φίλο μου", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιες είναι οι καταλήξεις αορίστου για ρήματα σε -AR;", "options_json": ["-é, -aste, -ó, -amos, -asteis, -aron", "-í, -iste, -ió, -imos, -isteis, -ieron", "-o, -as, -a, -amos, -áis, -an", "-ía, -ías, -ía, -íamos, -íais, -ían"], "correct_answer": "-é, -aste, -ó, -amos, -asteis, -aron", "explanation": "Αόριστος -AR: -é, -aste, -ó, -amos, -asteis, -aron", "points": 1},
                {"type": "fill_blank", "prompt": "¿Tú _____ la película? (Εσύ είδες την ταινία;) — ver → Αόριστος: vi, viste, vio...", "options_json": None, "correct_answer": "viste", "explanation": "Viste = είδες (2ο πρόσ. αόριστος του ver)", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «anoche» σημαίνει «απόψε».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Anoche = χθες βράδυ, όχι απόψε", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια πρόταση είναι στον αόριστο;", "options_json": ["Yo como una manzana", "Yo comí una manzana", "Yo voy a comer una manzana", "Yo estoy comiendo"], "correct_answer": "Yo comí una manzana", "explanation": "Comí = έφαγα (αόριστος)", "points": 1},
                {"type": "fill_blank", "prompt": "Ellos _____ a España la semana pasada. (Αυτοί ταξίδεψαν στην Ισπανία την περασμένη εβδομάδα) — viajar", "options_json": None, "correct_answer": "viajaron", "explanation": "Viajaron = ταξίδεψαν (3ο πληθ. αόριστος -AR)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Πέρσι έζησα στη Μαδρίτη»", "options_json": None, "correct_answer": "El año pasado viví en Madrid", "explanation": "El año pasado = πέρσι, viví = έζησα, en Madrid = στη Μαδρίτη", "points": 1},
                {"type": "true_false", "prompt": "Στον αόριστο, το «hablamos» μπορεί να σημαίνει «μιλάμε» (ενεστώτας) ή «μιλήσαμε» (αόριστος).", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Η 1η πληθυντικού σε -AR είναι η ίδια σε ενεστώτα και αόριστο", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «hace dos días»;", "options_json": ["Σε δύο μέρες", "Πριν δύο μέρες", "Δύο μέρες", "Κάθε δύο μέρες"], "correct_answer": "Πριν δύο μέρες", "explanation": "Hace + χρόνος = πριν...", "points": 1},
                {"type": "fill_blank", "prompt": "Yo _____ mucho ayer. (Διάβασα πολύ χθες) — estudiar", "options_json": None, "correct_answer": "estudié", "explanation": "Estudié = διάβασα (1ο πρόσ. αόριστος -AR)", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Pretérito Indefinido", "passing_score_pct": 60},
        },
        # ──────────────────────────────────────────────
        # CHAPTER 14 — Describing People
        # ──────────────────────────────────────────────
        {
            "order_index": 14,
            "title_greek": "Περιγραφή Ανθρώπων",
            "title_spanish": "Descripción de Personas",
            "difficulty_level": "intermediate",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Πώς Περιγράφουμε Ανθρώπους",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις πώς να περιγράφεις την εμφάνιση και τον χαρακτήρα ανθρώπων. Θα χρησιμοποιήσεις το ρήμα SER με επίθετα και θα μάθεις πώς τα επίθετα συμφωνούν σε γένος και αριθμό με το ουσιαστικό.",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Επίθετα Εξωτερικής Εμφάνισης",
                        "words": [
                            {"greek": "Ψηλός/Ψηλή", "spanish": "Alto/Alta", "pronunciation": "Άλτο/Άλτα"},
                            {"greek": "Κοντός/Κοντή", "spanish": "Bajo/Baja", "pronunciation": "Μπάχο/Μπάχα"},
                            {"greek": "Αδύνατος/Αδύνατη", "spanish": "Delgado/Delgada", "pronunciation": "Ντελγάδο/Ντελγάδα"},
                            {"greek": "Χοντρός/Χοντρή", "spanish": "Gordo/Gorda", "pronunciation": "Γκόρδο/Γκόρδα"},
                            {"greek": "Όμορφος/Όμορφη", "spanish": "Guapo/Guapa", "pronunciation": "Γκουάπο/Γκουάπα"},
                            {"greek": "Νέος/Νέα", "spanish": "Joven", "pronunciation": "Χόβεν"},
                            {"greek": "Ηλικιωμένος/η", "spanish": "Viejo/Vieja", "pronunciation": "Βιέχο/Βιέχα"},
                            {"greek": "Ξανθός/Ξανθιά", "spanish": "Rubio/Rubia", "pronunciation": "Ρούμπιο/Ρούμπια"},
                            {"greek": "Μελαχρινός/ή", "spanish": "Moreno/Morena", "pronunciation": "Μορένο/Μορένα"},
                            {"greek": "Κοκκινομάλλης/α", "spanish": "Pelirrojo/Pelirroja", "pronunciation": "Πελιρρόχο/Πελιρρόχα"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Επίθετα Χαρακτήρα",
                        "words": [
                            {"greek": "Έξυπνος/η", "spanish": "Inteligente", "pronunciation": "Ιντελιχέντε"},
                            {"greek": "Αστείος/α", "spanish": "Divertido/Divertida", "pronunciation": "Ντιβερτίδο/Ντιβερτίδα"},
                            {"greek": "Ντροπαλός/ή", "spanish": "Tímido/Tímida", "pronunciation": "Τίμιδο/Τίμιδα"},
                            {"greek": "Ευγενικός/ή", "spanish": "Amable", "pronunciation": "Αμάμπλε"},
                            {"greek": "Τεμπέλης/α", "spanish": "Perezoso/Perezosa", "pronunciation": "Περεθόσο/Περεθόσα"},
                            {"greek": "Εργατικός/ή", "spanish": "Trabajador/Trabajadora", "pronunciation": "Τραμπαχαδόρ/Τραμπαχαδόρα"},
                            {"greek": "Γενναιόδωρος/η", "spanish": "Generoso/Generosa", "pronunciation": "Χενερόσο/Χενερόσα"},
                            {"greek": "Σοβαρός/ή", "spanish": "Serio/Seria", "pronunciation": "Σέριο/Σέρια"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "SER + Επίθετο: Συμφωνία Γένους & Αριθμού",
                        "body": "Τα επίθετα στα Ισπανικά πρέπει να συμφωνούν με το ουσιαστικό σε γένος (αρσενικό/θηλυκό) και αριθμό (ενικός/πληθυντικός).",
                        "rules": [
                            "Επίθετα σε -o/-a: αλλάζουν γένος → alto/alta, guapo/guapa",
                            "Επίθετα σε -e: δεν αλλάζουν γένος → inteligente (και αρσ. και θηλ.)",
                            "Επίθετα σε σύμφωνο: συνήθως δεν αλλάζουν → joven (αλλά: trabajador/trabajadora)",
                            "Πληθυντικός: +s μετά φωνήεν, +es μετά σύμφωνο → altos, jóvenes",
                            "Él es alto y delgado. → Αυτός είναι ψηλός και αδύνατος.",
                            "Ella es alta y delgada. → Αυτή είναι ψηλή και αδύνατη.",
                            "Ellos son altos. → Αυτοί είναι ψηλοί.",
                            "Ellas son inteligentes. → Αυτές είναι έξυπνες.",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα Περιγραφών",
                        "examples": [
                            {"spanish": "Mi padre es alto y moreno. Es muy trabajador y amable.", "greek": "Ο πατέρας μου είναι ψηλός και μελαχρινός. Είναι πολύ εργατικός και ευγενικός."},
                            {"spanish": "Mi hermana es joven, rubia y muy divertida.", "greek": "Η αδερφή μου είναι νέα, ξανθιά και πολύ αστεία."},
                            {"spanish": "¿Cómo es tu mejor amigo?\n— Es bajo, moreno e inteligente.", "greek": "Πώς είναι ο καλύτερός σου φίλος;\n— Είναι κοντός, μελαχρινός και έξυπνος."},
                            {"spanish": "Mis abuelos son viejos pero muy generosos.", "greek": "Οι παππούδες μου είναι ηλικιωμένοι αλλά πολύ γενναιόδωροι."},
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Χρήσιμες Συμβουλές",
                        "tips": [
                            "Χρησιμοποίησε πάντα SER (όχι ESTAR) για μόνιμα χαρακτηριστικά: Es alto, es inteligente.",
                            "Πρόσεξε: «y» (και) γίνεται «e» πριν από λέξη που ξεκινά με i-/hi-: inteligente e interesante.",
                            "Τα επίθετα σε -e (inteligente, amable) είναι εύκολα γιατί δεν αλλάζουν!",
                            "Για να ρωτήσεις πώς είναι κάποιος (χαρακτήρας/εμφάνιση): ¿Cómo es? Για κατάσταση: ¿Cómo está?",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «ψηλός» στα Ισπανικά;", "options_json": ["Bajo", "Alto", "Gordo", "Delgado"], "correct_answer": "Alto", "explanation": "Alto = ψηλός", "points": 1},
                {"type": "fill_blank", "prompt": "Ella es _____ y rubia. (Αυτή είναι ψηλή και ξανθιά)", "options_json": None, "correct_answer": "alta", "explanation": "Alta = ψηλή (θηλυκό του alto)", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο επίθετο ΔΕΝ αλλάζει γένος;", "options_json": ["Alto/Alta", "Gordo/Gorda", "Inteligente", "Rubio/Rubia"], "correct_answer": "Inteligente", "explanation": "Τα επίθετα σε -e δεν αλλάζουν: inteligente", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «guapo» σημαίνει «κοντός».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Guapo = όμορφος. Κοντός = bajo.", "points": 1},
                {"type": "fill_blank", "prompt": "Mi hermano es muy _____. (Ο αδερφός μου είναι πολύ αστείος)", "options_json": None, "correct_answer": "divertido", "explanation": "Divertido = αστείος (αρσενικό)", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Αυτή είναι εργατική»;", "options_json": ["Ella es trabajador", "Ella es trabajadora", "Ella está trabajadora", "Ella es trabajando"], "correct_answer": "Ella es trabajadora", "explanation": "SER + θηλυκό: trabajadora", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Ο πατέρας μου είναι ψηλός»", "options_json": None, "correct_answer": "Mi padre es alto", "explanation": "Mi padre = ο πατέρας μου, es = είναι (SER), alto = ψηλός", "points": 1},
                {"type": "true_false", "prompt": "Η φράση «¿Cómo es?» ρωτά για μόνιμα χαρακτηριστικά (εμφάνιση/χαρακτήρα).", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "¿Cómo es? (SER) = πώς είναι (χαρακτηριστικά). ¿Cómo está? (ESTAR) = πώς είναι (κατάσταση).", "points": 1},
                {"type": "fill_blank", "prompt": "Mis hermanas son muy _____. (Οι αδερφές μου είναι πολύ ευγενικές)", "options_json": None, "correct_answer": "amables", "explanation": "Amables = ευγενικές (πληθ. του amable — δεν αλλάζει γένος)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «pelirrojo»;", "options_json": ["Ξανθός", "Μελαχρινός", "Κοκκινομάλλης", "Ψηλός"], "correct_answer": "Κοκκινομάλλης", "explanation": "Pelirrojo = κοκκινομάλλης (pelo = μαλλί + rojo = κόκκινο)", "points": 1},
                {"type": "true_false", "prompt": "Στα Ισπανικά, λέμε «Ella es alto» για μια ψηλή γυναίκα.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Σωστό: Ella es alta (θηλυκό)", "points": 1},
                {"type": "fill_blank", "prompt": "Ellos son _____ pero muy generosos. (Αυτοί είναι ηλικιωμένοι αλλά πολύ γενναιόδωροι)", "options_json": None, "correct_answer": "viejos", "explanation": "Viejos = ηλικιωμένοι (αρσ. πληθ.)", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Περιγραφή Ανθρώπων", "passing_score_pct": 60},
        },
        # ──────────────────────────────────────────────
        # CHAPTER 15 — Comprehensive Review
        # ──────────────────────────────────────────────
        {
            "order_index": 15,
            "title_greek": "Τελική Επανάληψη",
            "title_spanish": "Repaso Final",
            "difficulty_level": "intermediate",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Τελική Επανάληψη: Κεφάλαια 1-14",
                        "body": "Συγχαρητήρια! Έφτασες στο τελευταίο κεφάλαιο. Εδώ θα κάνεις μια συνολική επανάληψη όλων όσα έχεις μάθει μέχρι τώρα. Θα ανακεφαλαιώσουμε τη γραμματική, το λεξιλόγιο και τις βασικές δεξιότητες επικοινωνίας. Η τελική εξέταση θα περιλαμβάνει ερωτήσεις από όλα τα κεφάλαια!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "grammar",
                    "content_json": {
                        "title": "Ανακεφαλαίωση Γραμματικής",
                        "body": "Οι πιο σημαντικοί κανόνες που έχεις μάθει μέχρι τώρα.",
                        "rules": [
                            "SER vs ESTAR: SER = μόνιμα (εθνικότητα, επάγγελμα, χαρακτηριστικά). ESTAR = προσωρινά (τοποθεσία, συναισθήματα, κατάσταση).",
                            "Ρήματα -AR (ενεστ.): -o, -as, -a, -amos, -áis, -an. Π.χ. hablar → hablo, hablas...",
                            "Ρήματα -ER (ενεστ.): -o, -es, -e, -emos, -éis, -en. Π.χ. comer → como, comes...",
                            "Ρήματα -IR (ενεστ.): -o, -es, -e, -imos, -ís, -en. Π.χ. vivir → vivo, vives...",
                            "Ανώμαλα ρήματα: ir (voy, vas, va...), tener (tengo, tienes...), hacer (hago, haces...)",
                            "Αόριστος -AR: -é, -aste, -ó, -amos, -asteis, -aron",
                            "Αόριστος -ER/-IR: -í, -iste, -ió, -imos, -isteis, -ieron",
                            "Κτητικές: mi/mis, tu/tus, su/sus, nuestro(a)/nuestros(as)",
                            "Γένος επιθέτων: -o/-a αλλάζουν, -e και σύμφωνο συνήθως μένουν ίδια",
                            "Ir + a + απαρέμφατο = κοντινός μέλλοντας (Voy a comer = Θα φάω)",
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Ανακεφαλαίωση Βασικού Λεξιλογίου",
                        "words": [
                            {"greek": "Γεια σου / Αντίο", "spanish": "Hola / Adiós", "pronunciation": "Όλα / Αδιός"},
                            {"greek": "Ευχαριστώ / Παρακαλώ", "spanish": "Gracias / De nada", "pronunciation": "Γκράθιας / Ντε νάδα"},
                            {"greek": "Ναι / Όχι", "spanish": "Sí / No", "pronunciation": "Σι / Νο"},
                            {"greek": "Πώς σε λένε;", "spanish": "¿Cómo te llamas?", "pronunciation": "Κόμο τε γιάμας;"},
                            {"greek": "Πόσο κοστίζει;", "spanish": "¿Cuánto cuesta?", "pronunciation": "Κουάντο κουέστα;"},
                            {"greek": "Χθες / Σήμερα / Αύριο", "spanish": "Ayer / Hoy / Mañana", "pronunciation": "Αγιέρ / Όι / Μανιάνα"},
                            {"greek": "Πεινάω / Διψάω", "spanish": "Tengo hambre / Tengo sed", "pronunciation": "Τένγκο άμπρε / Τένγκο σεδ"},
                            {"greek": "Πού είναι;", "spanish": "¿Dónde está?", "pronunciation": "Ντόνδε εστά;"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "example",
                    "content_json": {
                        "title": "Σύνθετοι Διάλογοι Επανάληψης",
                        "examples": [
                            {
                                "spanish": "— ¡Hola! ¿Cómo te llamas?\n— Me llamo María. ¿Y tú?\n— Soy Carlos. ¿De dónde eres?\n— Soy griega, de Atenas. ¿Y tú?\n— Soy español, de Madrid.",
                                "greek": "— Γεια σου! Πώς σε λένε;\n— Με λένε Μαρία. Κι εσένα;\n— Είμαι ο Κάρλος. Από πού είσαι;\n— Είμαι Ελληνίδα, από την Αθήνα. Κι εσύ;\n— Είμαι Ισπανός, από τη Μαδρίτη.",
                            },
                            {
                                "spanish": "— ¿Qué hiciste ayer?\n— Fui al supermercado y compré comida. Después hice ejercicio.\n— ¿Y qué vas a hacer mañana?\n— Voy a ir a la playa con mi familia.",
                                "greek": "— Τι έκανες χθες;\n— Πήγα στο σούπερ μάρκετ και αγόρασα φαγητό. Μετά έκανα γυμναστική.\n— Και τι θα κάνεις αύριο;\n— Θα πάω στην παραλία με την οικογένειά μου.",
                            },
                            {
                                "spanish": "— ¿Cómo es tu hermano?\n— Es alto, moreno y muy divertido. Tiene veinticinco años.\n— ¿Dónde vive?\n— Vive en Barcelona. Es profesor.",
                                "greek": "— Πώς είναι ο αδερφός σου;\n— Είναι ψηλός, μελαχρινός και πολύ αστείος. Είναι είκοσι πέντε χρονών.\n— Πού μένει;\n— Μένει στη Βαρκελώνη. Είναι καθηγητής.",
                            },
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "tip",
                    "content_json": {
                        "title": "Στρατηγικές Μελέτης για Συνέχεια",
                        "tips": [
                            "Ξαναδιάβασε τα κεφάλαια που σου φάνηκαν δύσκολα πριν δώσεις την τελική εξέταση.",
                            "Προσπάθησε να μιλάς μόνος/η σου στα Ισπανικά — περίγραψε τη μέρα σου, τους φίλους σου, τα σχέδιά σου.",
                            "Άκου ισπανική μουσική ή δες ισπανικές σειρές με υπότιτλους για να συνηθίσεις τον ήχο της γλώσσας.",
                            "Κράτα ένα μικρό τετράδιο με νέες λέξεις που μαθαίνεις κάθε μέρα.",
                            "Μην φοβάσαι τα λάθη — είναι μέρος της μάθησης! Lo importante es practicar. (Το σημαντικό είναι να εξασκείσαι.)",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Καλημέρα» στα Ισπανικά;", "options_json": ["Buenas noches", "Buenos días", "Buenas tardes", "Hola"], "correct_answer": "Buenos días", "explanation": "Buenos días = Καλημέρα", "points": 1},
                {"type": "fill_blank", "prompt": "Yo _____ griego. (Είμαι Έλληνας — μόνιμο)", "options_json": None, "correct_answer": "soy", "explanation": "SER: Soy griego (εθνικότητα = μόνιμο)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «treinta y cinco»;", "options_json": ["25", "30", "35", "45"], "correct_answer": "35", "explanation": "Treinta y cinco = 35", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «hermana» σημαίνει «αδερφή».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Hermana = αδερφή", "points": 1},
                {"type": "fill_blank", "prompt": "Ella _____ en Madrid. (Αυτή είναι στη Μαδρίτη — τοποθεσία)", "options_json": None, "correct_answer": "está", "explanation": "ESTAR: Está en Madrid (τοποθεσία)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Πώς σε λένε;»", "options_json": None, "correct_answer": "¿Cómo te llamas?", "explanation": "¿Cómo te llamas? = Πώς σε λένε;", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο ρήμα χρησιμοποιούμε στη φράση «πεινάω» στα Ισπανικά;", "options_json": ["Ser", "Estar", "Tener", "Hacer"], "correct_answer": "Tener", "explanation": "Tengo hambre (έχω πείνα = πεινάω)", "points": 1},
                {"type": "fill_blank", "prompt": "Nosotros _____ al cine ayer. (Πήγαμε σινεμά χθες) — ir (αόριστος)", "options_json": None, "correct_answer": "fuimos", "explanation": "Fuimos = πήγαμε (αόριστος του ir)", "points": 1},
                {"type": "multiple_choice", "prompt": "«El libro rojo» σημαίνει:", "options_json": ["Το μπλε βιβλίο", "Το κόκκινο βιβλίο", "Η κόκκινη πόρτα", "Το πράσινο βιβλίο"], "correct_answer": "Το κόκκινο βιβλίο", "explanation": "El libro = το βιβλίο, rojo = κόκκινο", "points": 1},
                {"type": "true_false", "prompt": "Το «ir + a + απαρέμφατο» χρησιμοποιείται για τον κοντινό μέλλοντα.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Voy a comer = Θα φάω (κοντινός μέλλοντας)", "points": 1},
                {"type": "fill_blank", "prompt": "Mi madre _____ profesora. (Η μητέρα μου είναι δασκάλα — μόνιμο)", "options_json": None, "correct_answer": "es", "explanation": "SER: Es profesora (επάγγελμα = μόνιμο)", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια πρόταση είναι σωστή;", "options_json": ["Ella es alta y guapa", "Ella es alto y guapo", "Ella está alta", "Ella es alta y guapo"], "correct_answer": "Ella es alta y guapa", "explanation": "Θηλυκό: alta, guapa (SER για μόνιμα χαρακτηριστικά)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Χθες μίλησα με τη μητέρα μου»", "options_json": None, "correct_answer": "Ayer hablé con mi madre", "explanation": "Ayer = χθες, hablé = μίλησα, con mi madre = με τη μητέρα μου", "points": 1},
                {"type": "fill_blank", "prompt": "¿Cuánto _____ este libro? (Πόσο κοστίζει αυτό το βιβλίο;)", "options_json": None, "correct_answer": "cuesta", "explanation": "Cuesta = κοστίζει (ενικός)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «anoche»;", "options_json": ["Απόψε", "Χθες βράδυ", "Αύριο βράδυ", "Κάθε βράδυ"], "correct_answer": "Χθες βράδυ", "explanation": "Anoche = χθες βράδυ", "points": 1},
                {"type": "true_false", "prompt": "Τα επίθετα που τελειώνουν σε -e (inteligente, amable) αλλάζουν γένος.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Τα επίθετα σε -e δεν αλλάζουν: inteligente (αρσ. & θηλ.)", "points": 1},
                {"type": "fill_blank", "prompt": "Ellos _____ que estudiar. (Αυτοί πρέπει να διαβάσουν) — tener", "options_json": None, "correct_answer": "tienen", "explanation": "Tienen que + απαρέμφατο = πρέπει να", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιες κτητικές αντωνυμίες σημαίνουν «μου» (ενικ./πληθ.);", "options_json": ["Tu / Tus", "Mi / Mis", "Su / Sus", "El / La"], "correct_answer": "Mi / Mis", "explanation": "Mi = μου (ενικός), Mis = μου (πληθυντικός)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Κάνει ζέστη σήμερα»", "options_json": None, "correct_answer": "Hace calor hoy", "explanation": "Hacer calor = κάνει ζέστη, hoy = σήμερα", "points": 1},
                {"type": "fill_blank", "prompt": "Quinientos + trescientos = _____", "options_json": None, "correct_answer": "ochocientos", "explanation": "500 + 300 = 800 = ochocientos", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς ρωτάμε «Πού είναι;» στα Ισπανικά;", "options_json": ["¿Qué es?", "¿Cómo es?", "¿Dónde está?", "¿Cuándo es?"], "correct_answer": "¿Dónde está?", "explanation": "¿Dónde está? = Πού είναι; (ESTAR για τοποθεσία)", "points": 1},
                {"type": "true_false", "prompt": "Η πρόταση «Ayer comí paella» σημαίνει «Χθες θα φάω παέγια».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Comí = έφαγα (αόριστος), όχι θα φάω. Σωστό: Χθες έφαγα παέγια.", "points": 1},
                {"type": "fill_blank", "prompt": "Ella es _____, morena y muy amable. (Αυτή είναι νέα, μελαχρινή και πολύ ευγενική)", "options_json": None, "correct_answer": "joven", "explanation": "Joven = νέος/νέα (δεν αλλάζει γένος)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «Me lo llevo»;", "options_json": ["Θα το σκεφτώ", "Δεν το θέλω", "Θα το πάρω", "Είναι ακριβό"], "correct_answer": "Θα το πάρω", "explanation": "Me lo llevo = Θα το πάρω (σε κατάστημα)", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Αύριο θα πάω στην παραλία»", "options_json": None, "correct_answer": "Mañana voy a ir a la playa", "explanation": "Mañana = αύριο, voy a ir = θα πάω (ir + a + απαρέμφατο), a la playa = στην παραλία", "points": 1},
            ],
            "exam": {"title": "Τελική Εξέταση: Επανάληψη Κεφαλαίων 1-14", "passing_score_pct": 60},
        },
    ]

    for ch_data in chapters_data:
        chapter = Chapter(
            order_index=ch_data["order_index"],
            title_greek=ch_data["title_greek"],
            title_spanish=ch_data["title_spanish"],
            difficulty_level=ch_data["difficulty_level"],
        )
        db.add(chapter)
        db.flush()

        for sec_data in ch_data["sections"]:
            section = Section(
                chapter_id=chapter.id,
                order_index=sec_data["order_index"],
                type=sec_data["type"],
                content_json=sec_data["content_json"],
            )
            db.add(section)

        question_ids = []
        for q_data in ch_data["questions"]:
            question = Question(
                chapter_id=chapter.id,
                type=q_data["type"],
                prompt=q_data["prompt"],
                options_json=q_data["options_json"],
                correct_answer=q_data["correct_answer"],
                explanation=q_data.get("explanation"),
                points=q_data.get("points", 1),
            )
            db.add(question)
            db.flush()
            question_ids.append(question.id)

        exam_data = ch_data["exam"]
        exam = Exam(
            chapter_id=chapter.id,
            title=exam_data["title"],
            passing_score_pct=exam_data["passing_score_pct"],
            question_ids_json=question_ids,
        )
        db.add(exam)

    db.commit()
    db.close()
    print("Seed completed! Chapters 11-15 created with sections, questions and exams.")


if __name__ == "__main__":
    seed()
