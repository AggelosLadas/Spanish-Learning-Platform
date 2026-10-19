"""
Seed data for chapters 6-10 (elementary level).
Run: python -m app.db.seed_chapters_6_10
"""
from app.db.database import SessionLocal, engine, Base
from app.models.chapter import Chapter
from app.models.section import Section
from app.models.question import Question
from app.models.exam import Exam


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    existing = db.query(Chapter).filter(Chapter.order_index == 6).first()
    if existing:
        print("Chapter 6 already exists. Skipping seed for chapters 6-10.")
        db.close()
        return

    chapters_data = [
        # =====================================================================
        # CHAPTER 6 - Food & Drinks
        # =====================================================================
        {
            "order_index": 6,
            "title_greek": "Τρόφιμα και Ποτά",
            "title_spanish": "Alimentos y Bebidas",
            "difficulty_level": "elementary",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή: Τρόφιμα και Ποτά",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις βασικό λεξιλόγιο σχετικά με φαγητά και ποτά στα Ισπανικά. Θα δεις επίσης πώς να παραγγέλνεις σε μια καφετέρια ή εστιατόριο χρησιμοποιώντας φράσεις όπως «Quiero...» (Θέλω...) και «Me gustaría...» (Θα ήθελα...).",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Τρόφιμα",
                        "words": [
                            {"greek": "Ψωμί", "spanish": "El pan", "pronunciation": "Ελ παν"},
                            {"greek": "Γάλα", "spanish": "La leche", "pronunciation": "Λα λέτσε"},
                            {"greek": "Τυρί", "spanish": "El queso", "pronunciation": "Ελ κέσο"},
                            {"greek": "Κρέας", "spanish": "La carne", "pronunciation": "Λα κάρνε"},
                            {"greek": "Ψάρι", "spanish": "El pescado", "pronunciation": "Ελ πεσκάδο"},
                            {"greek": "Ρύζι", "spanish": "El arroz", "pronunciation": "Ελ αρόθ"},
                            {"greek": "Αυγό", "spanish": "El huevo", "pronunciation": "Ελ ουέβο"},
                            {"greek": "Σαλάτα", "spanish": "La ensalada", "pronunciation": "Λα ενσαλάδα"},
                            {"greek": "Φρούτο", "spanish": "La fruta", "pronunciation": "Λα φρούτα"},
                            {"greek": "Σάντουιτς", "spanish": "El bocadillo", "pronunciation": "Ελ μποκαδίγιο"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Ποτά",
                        "words": [
                            {"greek": "Νερό", "spanish": "El agua", "pronunciation": "Ελ άγκουα"},
                            {"greek": "Καφές", "spanish": "El café", "pronunciation": "Ελ καφέ"},
                            {"greek": "Τσάι", "spanish": "El té", "pronunciation": "Ελ τε"},
                            {"greek": "Χυμός", "spanish": "El zumo", "pronunciation": "Ελ θούμο"},
                            {"greek": "Μπύρα", "spanish": "La cerveza", "pronunciation": "Λα θερβέθα"},
                            {"greek": "Κρασί", "spanish": "El vino", "pronunciation": "Ελ βίνο"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Φράσεις Παραγγελίας",
                        "body": "Στα Ισπανικά υπάρχουν διάφοροι τρόποι να παραγγείλεις, από απλούς έως πιο ευγενικούς.",
                        "rules": [
                            "Quiero... → Θέλω... (απλός/άμεσος τρόπος)",
                            "Me gustaría... → Θα ήθελα... (πιο ευγενικός τρόπος)",
                            "¿Me puede traer...? → Μπορείτε να μου φέρετε...;",
                            "Quisiera... → Θα επιθυμούσα... (πολύ ευγενικός)",
                            "La cuenta, por favor. → Τον λογαριασμό, παρακαλώ.",
                            "¿Cuánto cuesta? → Πόσο κοστίζει;",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Διάλογος σε Καφετέρια",
                        "examples": [
                            {
                                "spanish": "— Buenos días. ¿Qué desea?\n— Me gustaría un café con leche, por favor.\n— ¿Algo más?\n— Sí, un bocadillo de queso.\n— Muy bien. Son tres euros con cincuenta.",
                                "greek": "— Καλημέρα. Τι θα θέλατε;\n— Θα ήθελα έναν καφέ με γάλα, παρακαλώ.\n— Κάτι άλλο;\n— Ναι, ένα σάντουιτς με τυρί.\n— Πολύ ωραία. Κάνει τρία ευρώ και πενήντα.",
                            },
                            {
                                "spanish": "— Quiero un zumo de naranja y una ensalada, por favor.\n— ¿De beber, algo más?\n— No, gracias. La cuenta, por favor.",
                                "greek": "— Θέλω έναν χυμό πορτοκάλι και μια σαλάτα, παρακαλώ.\n— Από ποτό, κάτι άλλο;\n— Όχι, ευχαριστώ. Τον λογαριασμό, παρακαλώ.",
                            },
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Χρήσιμες Συμβουλές",
                        "tips": [
                            "Στην Ισπανία, το «el agua» είναι θηλυκό αλλά παίρνει αρσενικό άρθρο (el) λόγω προφοράς — la agua ακούγεται δύσκολα, γι' αυτό λέμε el agua.",
                            "Το «zumo» χρησιμοποιείται στην Ισπανία, ενώ στη Λατινική Αμερική λένε «jugo».",
                            "Πάντα λέγε «por favor» (παρακαλώ) — η ευγένεια εκτιμάται πολύ στον ισπανόφωνο κόσμο!",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Ψωμί» στα Ισπανικά;", "options_json": ["La leche", "El pan", "El queso", "La carne"], "correct_answer": "El pan", "explanation": "El pan = Ψωμί", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «el agua»;", "options_json": ["Γάλα", "Χυμός", "Νερό", "Τσάι"], "correct_answer": "Νερό", "explanation": "El agua = Νερό", "points": 1},
                {"type": "fill_blank", "prompt": "Me gustaría un _____ con leche. (καφέ)", "options_json": None, "correct_answer": "café", "explanation": "Café = καφές", "points": 1},
                {"type": "true_false", "prompt": "Η φράση «Quiero» σημαίνει «Θα ήθελα».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Quiero = Θέλω. Θα ήθελα = Me gustaría.", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Τυρί» στα Ισπανικά;", "options_json": ["El arroz", "La fruta", "El queso", "El huevo"], "correct_answer": "El queso", "explanation": "El queso = Τυρί", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Τον λογαριασμό, παρακαλώ.»", "options_json": None, "correct_answer": "La cuenta, por favor.", "explanation": "La cuenta, por favor = Τον λογαριασμό, παρακαλώ.", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «la cerveza»;", "options_json": ["Καφές", "Χυμός", "Μπύρα", "Κρασί"], "correct_answer": "Μπύρα", "explanation": "La cerveza = Μπύρα", "points": 1},
                {"type": "fill_blank", "prompt": "Quiero un _____ de naranja. (χυμό)", "options_json": None, "correct_answer": "zumo", "explanation": "Zumo = χυμός", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «bocadillo» σημαίνει «σαλάτα».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Bocadillo = σάντουιτς, ensalada = σαλάτα.", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς παραγγέλνουμε ευγενικά στα Ισπανικά;", "options_json": ["Quiero...", "Tengo...", "Me gustaría...", "Soy..."], "correct_answer": "Me gustaría...", "explanation": "Me gustaría... = Θα ήθελα... (ευγενικός τρόπος)", "points": 1},
                {"type": "fill_blank", "prompt": "¿Cuánto _____? (Πόσο κοστίζει;)", "options_json": None, "correct_answer": "cuesta", "explanation": "¿Cuánto cuesta? = Πόσο κοστίζει;", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «el huevo»;", "options_json": ["Ψάρι", "Αυγό", "Ρύζι", "Κρέας"], "correct_answer": "Αυγό", "explanation": "El huevo = Αυγό", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Τρόφιμα και Ποτά", "passing_score_pct": 60},
        },
        # =====================================================================
        # CHAPTER 7 - Days & Months
        # =====================================================================
        {
            "order_index": 7,
            "title_greek": "Μέρες και Μήνες",
            "title_spanish": "Días y Meses",
            "difficulty_level": "elementary",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή: Μέρες και Μήνες",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις τις μέρες της εβδομάδας και τους μήνες του χρόνου στα Ισπανικά. Θα μάθεις επίσης πώς να ρωτάς και να λες ημερομηνίες. Στα Ισπανικά, οι μέρες και οι μήνες γράφονται πάντα με πεζό αρχικό γράμμα!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Μέρες της Εβδομάδας",
                        "words": [
                            {"greek": "Δευτέρα", "spanish": "Lunes", "pronunciation": "Λούνες"},
                            {"greek": "Τρίτη", "spanish": "Martes", "pronunciation": "Μάρτες"},
                            {"greek": "Τετάρτη", "spanish": "Miércoles", "pronunciation": "Μιέρκολες"},
                            {"greek": "Πέμπτη", "spanish": "Jueves", "pronunciation": "Χουέβες"},
                            {"greek": "Παρασκευή", "spanish": "Viernes", "pronunciation": "Βιέρνες"},
                            {"greek": "Σάββατο", "spanish": "Sábado", "pronunciation": "Σάμπαδο"},
                            {"greek": "Κυριακή", "spanish": "Domingo", "pronunciation": "Ντομίνγκο"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Μήνες του Χρόνου",
                        "words": [
                            {"greek": "Ιανουάριος", "spanish": "Enero", "pronunciation": "Ενέρο"},
                            {"greek": "Φεβρουάριος", "spanish": "Febrero", "pronunciation": "Φεμπρέρο"},
                            {"greek": "Μάρτιος", "spanish": "Marzo", "pronunciation": "Μάρθο"},
                            {"greek": "Απρίλιος", "spanish": "Abril", "pronunciation": "Αμπρίλ"},
                            {"greek": "Μάιος", "spanish": "Mayo", "pronunciation": "Μάγιο"},
                            {"greek": "Ιούνιος", "spanish": "Junio", "pronunciation": "Χούνιο"},
                            {"greek": "Ιούλιος", "spanish": "Julio", "pronunciation": "Χούλιο"},
                            {"greek": "Αύγουστος", "spanish": "Agosto", "pronunciation": "Αγκόστο"},
                            {"greek": "Σεπτέμβριος", "spanish": "Septiembre", "pronunciation": "Σεπτιέμπρε"},
                            {"greek": "Οκτώβριος", "spanish": "Octubre", "pronunciation": "Οκτούμπρε"},
                            {"greek": "Νοέμβριος", "spanish": "Noviembre", "pronunciation": "Νοβιέμπρε"},
                            {"greek": "Δεκέμβριος", "spanish": "Diciembre", "pronunciation": "Ντιθιέμπρε"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Εκφράσεις Ημερομηνίας",
                        "body": "Μάθε πώς να ρωτάς και να λες τι μέρα/ημερομηνία είναι στα Ισπανικά.",
                        "rules": [
                            "¿Qué día es hoy? → Τι μέρα είναι σήμερα;",
                            "Hoy es lunes. → Σήμερα είναι Δευτέρα.",
                            "¿Cuál es la fecha de hoy? → Ποια είναι η σημερινή ημερομηνία;",
                            "Hoy es el 15 de marzo. → Σήμερα είναι 15 Μαρτίου.",
                            "Mi cumpleaños es el 3 de julio. → Τα γενέθλιά μου είναι στις 3 Ιουλίου.",
                            "Ayer fue domingo. → Χθες ήταν Κυριακή.",
                            "Mañana es miércoles. → Αύριο είναι Τετάρτη.",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "tip",
                    "content_json": {
                        "title": "Χρήσιμες Συμβουλές",
                        "tips": [
                            "Στα Ισπανικά οι μέρες και οι μήνες γράφονται ΠΑΝΤΑ με πεζό γράμμα: lunes, enero (σε αντίθεση με τα Αγγλικά).",
                            "Η εβδομάδα ξεκινάει από Δευτέρα (lunes), όπως στην Ελλάδα.",
                            "Οι ημερομηνίες λέγονται: el + αριθμός + de + μήνας (π.χ. el 5 de mayo).",
                            "Η μόνη εξαίρεση είναι η 1η του μήνα: el primero de enero (η πρώτη Ιανουαρίου).",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Δευτέρα» στα Ισπανικά;", "options_json": ["Martes", "Lunes", "Miércoles", "Viernes"], "correct_answer": "Lunes", "explanation": "Lunes = Δευτέρα", "points": 1},
                {"type": "fill_blank", "prompt": "Hoy es _____. (Σήμερα είναι Παρασκευή)", "options_json": None, "correct_answer": "viernes", "explanation": "Viernes = Παρασκευή", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιος μήνας είναι ο «marzo»;", "options_json": ["Μάιος", "Μάρτιος", "Απρίλιος", "Φεβρουάριος"], "correct_answer": "Μάρτιος", "explanation": "Marzo = Μάρτιος", "points": 1},
                {"type": "true_false", "prompt": "Στα Ισπανικά, οι μέρες της εβδομάδας γράφονται με κεφαλαίο αρχικό γράμμα.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Γράφονται πάντα με πεζό: lunes, martes κ.λπ.", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς ρωτάμε «Τι μέρα είναι σήμερα;» στα Ισπανικά;", "options_json": ["¿Cómo estás?", "¿Qué día es hoy?", "¿Cuántos años tienes?", "¿Cómo te llamas?"], "correct_answer": "¿Qué día es hoy?", "explanation": "¿Qué día es hoy? = Τι μέρα είναι σήμερα;", "points": 1},
                {"type": "fill_blank", "prompt": "Mi cumpleaños es el 3 de _____. (Ιουλίου)", "options_json": None, "correct_answer": "julio", "explanation": "Julio = Ιούλιος", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Σήμερα είναι 15 Μαρτίου.»", "options_json": None, "correct_answer": "Hoy es el 15 de marzo.", "explanation": "Hoy es el + αριθμός + de + μήνας", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια μέρα έρχεται μετά τη «jueves»;", "options_json": ["Miércoles", "Sábado", "Viernes", "Domingo"], "correct_answer": "Viernes", "explanation": "Μετά την Πέμπτη (jueves) είναι η Παρασκευή (viernes)", "points": 1},
                {"type": "true_false", "prompt": "Ο μήνας «diciembre» αντιστοιχεί στον Νοέμβριο.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Diciembre = Δεκέμβριος, noviembre = Νοέμβριος.", "points": 1},
                {"type": "fill_blank", "prompt": "¿Qué día es _____? (σήμερα)", "options_json": None, "correct_answer": "hoy", "explanation": "Hoy = σήμερα", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Μέρες και Μήνες", "passing_score_pct": 60},
        },
        # =====================================================================
        # CHAPTER 8 - Regular -AR Verbs
        # =====================================================================
        {
            "order_index": 8,
            "title_greek": "Ρήματα AR στον Ενεστώτα",
            "title_spanish": "Verbos Regulares en -AR",
            "difficulty_level": "elementary",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή: Ρήματα σε -AR",
                        "body": "Τα ρήματα σε -AR είναι η πιο κοινή κατηγορία ρημάτων στα Ισπανικά. Σε αυτό το κεφάλαιο θα μάθεις πώς να κλίνεις κανονικά ρήματα σε -AR στον Ενεστώτα (Presente de Indicativo). Μόλις μάθεις το μοτίβο, μπορείς να κλίνεις εκατοντάδες ρήματα!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "grammar",
                    "content_json": {
                        "title": "Μοτίβο Κλίσης Ρημάτων σε -AR",
                        "body": "Για να κλίνεις ένα ρήμα σε -AR, αφαιρείς την κατάληξη -ar και προσθέτεις τις αντίστοιχες καταλήξεις. Παράδειγμα: HABLAR (μιλάω)",
                        "rules": [
                            "Yo habl-o → Εγώ μιλάω",
                            "Tú habl-as → Εσύ μιλάς",
                            "Él/Ella habl-a → Αυτός/Αυτή μιλάει",
                            "Nosotros habl-amos → Εμείς μιλάμε",
                            "Vosotros habl-áis → Εσείς μιλάτε",
                            "Ellos/Ellas habl-an → Αυτοί/Αυτές μιλάνε",
                            "Καταλήξεις: -o, -as, -a, -amos, -áis, -an",
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Κοινά Ρήματα σε -AR",
                        "words": [
                            {"greek": "Μιλάω", "spanish": "Hablar", "pronunciation": "Αμπλάρ"},
                            {"greek": "Δουλεύω", "spanish": "Trabajar", "pronunciation": "Τραμπαχάρ"},
                            {"greek": "Περπατάω", "spanish": "Caminar", "pronunciation": "Καμινάρ"},
                            {"greek": "Σπουδάζω", "spanish": "Estudiar", "pronunciation": "Εστουδιάρ"},
                            {"greek": "Μαγειρεύω", "spanish": "Cocinar", "pronunciation": "Κοθινάρ"},
                            {"greek": "Χορεύω", "spanish": "Bailar", "pronunciation": "Μπαϊλάρ"},
                            {"greek": "Τραγουδάω", "spanish": "Cantar", "pronunciation": "Καντάρ"},
                            {"greek": "Ταξιδεύω", "spanish": "Viajar", "pronunciation": "Βιαχάρ"},
                            {"greek": "Αγοράζω", "spanish": "Comprar", "pronunciation": "Κομπράρ"},
                            {"greek": "Πληρώνω", "spanish": "Pagar", "pronunciation": "Παγκάρ"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα σε Προτάσεις",
                        "examples": [
                            {"spanish": "Yo hablo español.", "greek": "Εγώ μιλάω Ισπανικά."},
                            {"spanish": "Tú trabajas en una oficina.", "greek": "Εσύ δουλεύεις σε ένα γραφείο."},
                            {"spanish": "Ella estudia medicina.", "greek": "Αυτή σπουδάζει ιατρική."},
                            {"spanish": "Nosotros caminamos por el parque.", "greek": "Εμείς περπατάμε στο πάρκο."},
                            {"spanish": "Ellos viajan a España.", "greek": "Αυτοί ταξιδεύουν στην Ισπανία."},
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "grammar",
                    "content_json": {
                        "title": "Δομή Πρότασης με Ρήματα -AR",
                        "body": "Στα Ισπανικά, η βασική σειρά είναι Υποκείμενο + Ρήμα + Αντικείμενο, αλλά συχνά το υποκείμενο παραλείπεται γιατί η κατάληξη του ρήματος δείχνει ποιος μιλάει.",
                        "rules": [
                            "Hablo español. → Μιλάω Ισπανικά. (χωρίς «yo» — η κατάληξη -o δείχνει ότι εγώ)",
                            "¿Hablas inglés? → Μιλάς Αγγλικά; (η κατάληξη -as δείχνει ότι εσύ)",
                            "No hablamos francés. → Δεν μιλάμε Γαλλικά. (Αρνητική: No + ρήμα)",
                            "¿Trabajas o estudias? → Δουλεύεις ή σπουδάζεις;",
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Συμβουλές Εκμάθησης",
                        "tips": [
                            "Αποστήθισε τις καταλήξεις -o, -as, -a, -amos, -áis, -an — ισχύουν για ΟΛΑ τα κανονικά ρήματα σε -AR!",
                            "Στον προφορικό λόγο, οι Ισπανοί σπάνια λένε το υποκείμενο (yo, tú κ.λπ.) γιατί η κατάληξη αρκεί.",
                            "Δοκίμασε να φτιάξεις δικές σου προτάσεις κάθε μέρα — π.χ. «Estudio español» (Σπουδάζω Ισπανικά).",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Ποια είναι η κατάληξη για «yo» στα ρήματα σε -AR;", "options_json": ["-as", "-o", "-a", "-amos"], "correct_answer": "-o", "explanation": "Yo habl-o → κατάληξη -o", "points": 1},
                {"type": "fill_blank", "prompt": "Tú habl_____ español. (Εσύ μιλάς Ισπανικά)", "options_json": None, "correct_answer": "as", "explanation": "Tú + κατάληξη -as → hablas", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς κλίνεται το «trabajar» για «nosotros»;", "options_json": ["Trabajas", "Trabajo", "Trabajamos", "Trabajan"], "correct_answer": "Trabajamos", "explanation": "Nosotros trabaj-amos", "points": 1},
                {"type": "fill_blank", "prompt": "Ella estudi_____ medicina. (Αυτή σπουδάζει ιατρική)", "options_json": None, "correct_answer": "a", "explanation": "Ella + κατάληξη -a → estudia", "points": 1},
                {"type": "true_false", "prompt": "Η κατάληξη «-an» αντιστοιχεί στο «nosotros».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Nosotros → -amos. Η κατάληξη -an αντιστοιχεί στο ellos/ellas.", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «cocinar»;", "options_json": ["Χορεύω", "Μαγειρεύω", "Τραγουδάω", "Πληρώνω"], "correct_answer": "Μαγειρεύω", "explanation": "Cocinar = Μαγειρεύω", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Εμείς χορεύουμε.»", "options_json": None, "correct_answer": "Nosotros bailamos.", "explanation": "Bailar (χορεύω) → nosotros bail-amos", "points": 1},
                {"type": "fill_blank", "prompt": "Ellos camin_____ por la playa. (Αυτοί περπατούν στην παραλία)", "options_json": None, "correct_answer": "an", "explanation": "Ellos + κατάληξη -an → caminan", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Δεν μιλάω Γαλλικά» στα Ισπανικά;", "options_json": ["Hablo no francés", "No hablo francés", "Hablo francés no", "Francés no hablo"], "correct_answer": "No hablo francés", "explanation": "Αρνητική: No + ρήμα → No hablo francés", "points": 1},
                {"type": "true_false", "prompt": "Στα Ισπανικά πρέπει πάντα να λέμε το υποκείμενο (yo, tú κ.λπ.).", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Συχνά παραλείπεται γιατί η κατάληξη του ρήματος δείχνει το πρόσωπο.", "points": 1},
                {"type": "fill_blank", "prompt": "Yo compr_____ fruta. (Εγώ αγοράζω φρούτα)", "options_json": None, "correct_answer": "o", "explanation": "Yo + κατάληξη -o → compro", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο ρήμα σημαίνει «Ταξιδεύω»;", "options_json": ["Caminar", "Bailar", "Viajar", "Pagar"], "correct_answer": "Viajar", "explanation": "Viajar = Ταξιδεύω", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Αυτή τραγουδάει.»", "options_json": None, "correct_answer": "Ella canta.", "explanation": "Cantar (τραγουδάω) → ella cant-a", "points": 1},
                {"type": "multiple_choice", "prompt": "«Vosotros habláis» σημαίνει:", "options_json": ["Εμείς μιλάμε", "Εσείς μιλάτε", "Αυτοί μιλάνε", "Εσύ μιλάς"], "correct_answer": "Εσείς μιλάτε", "explanation": "Vosotros habláis = Εσείς μιλάτε", "points": 1},
                {"type": "fill_blank", "prompt": "¿Tú trabaj_____ o estudi_____? (Δουλεύεις ή σπουδάζεις;)", "options_json": None, "correct_answer": "as", "explanation": "Tú + κατάληξη -as → trabajas, estudias", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Ρήματα AR στον Ενεστώτα", "passing_score_pct": 60},
        },
        # =====================================================================
        # CHAPTER 9 - Regular -ER/-IR Verbs
        # =====================================================================
        {
            "order_index": 9,
            "title_greek": "Ρήματα ER/IR στον Ενεστώτα",
            "title_spanish": "Verbos Regulares en -ER/-IR",
            "difficulty_level": "elementary",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή: Ρήματα σε -ER και -IR",
                        "body": "Μετά τα ρήματα σε -AR, οι δύο άλλες κατηγορίες κανονικών ρημάτων είναι τα ρήματα σε -ER και -IR. Οι κλίσεις τους είναι πολύ παρόμοιες μεταξύ τους και διαφέρουν ελαφρώς από τα -AR. Μόλις τα μάθεις, θα μπορείς να κλίνεις τη μεγάλη πλειονότητα των ισπανικών ρημάτων!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση Ρημάτων σε -ER",
                        "body": "Παράδειγμα: COMER (τρώω). Αφαιρούμε το -er και προσθέτουμε τις καταλήξεις.",
                        "rules": [
                            "Yo com-o → Εγώ τρώω",
                            "Tú com-es → Εσύ τρως",
                            "Él/Ella com-e → Αυτός/Αυτή τρώει",
                            "Nosotros com-emos → Εμείς τρώμε",
                            "Vosotros com-éis → Εσείς τρώτε",
                            "Ellos/Ellas com-en → Αυτοί/Αυτές τρώνε",
                            "Καταλήξεις -ER: -o, -es, -e, -emos, -éis, -en",
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση Ρημάτων σε -IR",
                        "body": "Παράδειγμα: VIVIR (ζω). Οι καταλήξεις των -IR μοιάζουν πολύ με τα -ER, με μικρές διαφορές στο nosotros και vosotros.",
                        "rules": [
                            "Yo viv-o → Εγώ ζω",
                            "Tú viv-es → Εσύ ζεις",
                            "Él/Ella viv-e → Αυτός/Αυτή ζει",
                            "Nosotros viv-imos → Εμείς ζούμε",
                            "Vosotros viv-ís → Εσείς ζείτε",
                            "Ellos/Ellas viv-en → Αυτοί/Αυτές ζουν",
                            "Καταλήξεις -IR: -o, -es, -e, -imos, -ís, -en",
                            "Διαφορά -ER vs -IR: nosotros (-emos vs -imos) και vosotros (-éis vs -ís)",
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "vocab",
                    "content_json": {
                        "title": "Κοινά Ρήματα σε -ER και -IR",
                        "words": [
                            {"greek": "Τρώω", "spanish": "Comer", "pronunciation": "Κομέρ"},
                            {"greek": "Πίνω", "spanish": "Beber", "pronunciation": "Μπεμπέρ"},
                            {"greek": "Διαβάζω", "spanish": "Leer", "pronunciation": "Λεέρ"},
                            {"greek": "Μαθαίνω", "spanish": "Aprender", "pronunciation": "Απρεντέρ"},
                            {"greek": "Καταλαβαίνω", "spanish": "Comprender", "pronunciation": "Κομπρεντέρ"},
                            {"greek": "Ζω", "spanish": "Vivir", "pronunciation": "Βιβίρ"},
                            {"greek": "Γράφω", "spanish": "Escribir", "pronunciation": "Εσκριβίρ"},
                            {"greek": "Ανοίγω", "spanish": "Abrir", "pronunciation": "Αμπρίρ"},
                            {"greek": "Λαμβάνω", "spanish": "Recibir", "pronunciation": "Ρεθιβίρ"},
                            {"greek": "Μοιράζομαι", "spanish": "Compartir", "pronunciation": "Κομπαρτίρ"},
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα σε Προτάσεις",
                        "examples": [
                            {"spanish": "Yo como paella los domingos.", "greek": "Εγώ τρώω παέγια τις Κυριακές."},
                            {"spanish": "Tú bebes mucha agua.", "greek": "Εσύ πίνεις πολύ νερό."},
                            {"spanish": "Ella escribe una carta.", "greek": "Αυτή γράφει ένα γράμμα."},
                            {"spanish": "Nosotros vivimos en Atenas.", "greek": "Εμείς ζούμε στην Αθήνα."},
                            {"spanish": "Ellos aprenden español rápido.", "greek": "Αυτοί μαθαίνουν Ισπανικά γρήγορα."},
                            {"spanish": "¿Comprendes la lección?", "greek": "Καταλαβαίνεις το μάθημα;"},
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Συμβουλές Εκμάθησης",
                        "tips": [
                            "Οι καταλήξεις -ER και -IR είναι ίδιες σε 4 από τα 6 πρόσωπα — μόνο το nosotros και vosotros διαφέρουν!",
                            "Το πρώτο πρόσωπο ενικού (yo) τελειώνει πάντα σε -o, σε ΟΛΕΣ τις κατηγορίες (-AR, -ER, -IR).",
                            "Φτιάξε έναν πίνακα με τις τρεις κατηγορίες δίπλα-δίπλα για να δεις τις ομοιότητες.",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Ποια είναι η κατάληξη για «tú» στα ρήματα σε -ER;", "options_json": ["-as", "-es", "-is", "-os"], "correct_answer": "-es", "explanation": "Tú com-es → κατάληξη -es", "points": 1},
                {"type": "fill_blank", "prompt": "Yo com_____ paella. (Εγώ τρώω παέγια)", "options_json": None, "correct_answer": "o", "explanation": "Yo + κατάληξη -o → como", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς κλίνεται το «vivir» για «nosotros»;", "options_json": ["Vivemos", "Vivimos", "Viven", "Vivís"], "correct_answer": "Vivimos", "explanation": "Nosotros viv-imos (κατάληξη -IR: -imos)", "points": 1},
                {"type": "fill_blank", "prompt": "Ella escrib_____ una carta. (Αυτή γράφει ένα γράμμα)", "options_json": None, "correct_answer": "e", "explanation": "Ella + κατάληξη -e → escribe", "points": 1},
                {"type": "true_false", "prompt": "Οι καταλήξεις -ER και -IR είναι ίδιες σε όλα τα πρόσωπα.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Διαφέρουν στο nosotros (-emos vs -imos) και vosotros (-éis vs -ís).", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «beber»;", "options_json": ["Τρώω", "Πίνω", "Γράφω", "Ζω"], "correct_answer": "Πίνω", "explanation": "Beber = Πίνω", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Εσύ πίνεις νερό.»", "options_json": None, "correct_answer": "Tú bebes agua.", "explanation": "Beber (πίνω) → tú beb-es", "points": 1},
                {"type": "fill_blank", "prompt": "Nosotros aprend_____ español. (Εμείς μαθαίνουμε Ισπανικά)", "options_json": None, "correct_answer": "emos", "explanation": "Nosotros + κατάληξη -emos → aprendemos", "points": 1},
                {"type": "multiple_choice", "prompt": "«Ellos escriben» σημαίνει:", "options_json": ["Αυτοί διαβάζουν", "Αυτοί γράφουν", "Αυτοί ζουν", "Αυτοί τρώνε"], "correct_answer": "Αυτοί γράφουν", "explanation": "Escribir = γράφω, ellos escriben = αυτοί γράφουν", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «leer» σημαίνει «γράφω».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Leer = διαβάζω, escribir = γράφω.", "points": 1},
                {"type": "fill_blank", "prompt": "Tú viv_____ en Madrid. (Εσύ ζεις στη Μαδρίτη)", "options_json": None, "correct_answer": "es", "explanation": "Tú + κατάληξη -es → vives", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο ρήμα σημαίνει «Ανοίγω»;", "options_json": ["Vivir", "Abrir", "Escribir", "Recibir"], "correct_answer": "Abrir", "explanation": "Abrir = Ανοίγω", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Αυτοί ζουν στην Ισπανία.»", "options_json": None, "correct_answer": "Ellos viven en España.", "explanation": "Vivir (ζω) → ellos viv-en", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια κατάληξη παίρνει το «vosotros» στα ρήματα σε -IR;", "options_json": ["-éis", "-ís", "-en", "-emos"], "correct_answer": "-ís", "explanation": "Vosotros viv-ís → κατάληξη -ís", "points": 1},
                {"type": "fill_blank", "prompt": "Ellos comprend_____ todo. (Αυτοί καταλαβαίνουν τα πάντα)", "options_json": None, "correct_answer": "en", "explanation": "Ellos + κατάληξη -en → comprenden", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Ρήματα ER/IR στον Ενεστώτα", "passing_score_pct": 60},
        },
        # =====================================================================
        # CHAPTER 10 - Directions & Transport
        # =====================================================================
        {
            "order_index": 10,
            "title_greek": "Κατεύθυνση και Μεταφορά",
            "title_spanish": "Direcciones y Transporte",
            "difficulty_level": "elementary",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή: Κατεύθυνση και Μεταφορά",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις πώς να ρωτάς και να δίνεις οδηγίες κατεύθυνσης, καθώς και βασικό λεξιλόγιο για τα μέσα μεταφοράς. Αυτές οι γνώσεις είναι απαραίτητες όταν ταξιδεύεις σε ισπανόφωνες χώρες!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Κατευθύνσεις",
                        "words": [
                            {"greek": "Αριστερά", "spanish": "Izquierda", "pronunciation": "Ιθκιέρδα"},
                            {"greek": "Δεξιά", "spanish": "Derecha", "pronunciation": "Ντερέτσα"},
                            {"greek": "Ευθεία / Ίσια", "spanish": "Recto / Derecho", "pronunciation": "Ρέκτο / Ντερέτσο"},
                            {"greek": "Κοντά", "spanish": "Cerca", "pronunciation": "Θέρκα"},
                            {"greek": "Μακριά", "spanish": "Lejos", "pronunciation": "Λέχος"},
                            {"greek": "Δίπλα σε", "spanish": "Al lado de", "pronunciation": "Αλ λάδο ντε"},
                            {"greek": "Μπροστά από", "spanish": "Delante de / Enfrente de", "pronunciation": "Ντελάντε ντε / Ενφρέντε ντε"},
                            {"greek": "Πίσω από", "spanish": "Detrás de", "pronunciation": "Ντετράς ντε"},
                            {"greek": "Στη γωνία", "spanish": "En la esquina", "pronunciation": "Εν λα εσκίνα"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Μέσα Μεταφοράς",
                        "words": [
                            {"greek": "Λεωφορείο", "spanish": "El autobús", "pronunciation": "Ελ αουτομπούς"},
                            {"greek": "Μετρό", "spanish": "El metro", "pronunciation": "Ελ μέτρο"},
                            {"greek": "Τρένο", "spanish": "El tren", "pronunciation": "Ελ τρεν"},
                            {"greek": "Ταξί", "spanish": "El taxi", "pronunciation": "Ελ τάξι"},
                            {"greek": "Αεροπλάνο", "spanish": "El avión", "pronunciation": "Ελ αβιόν"},
                            {"greek": "Ποδήλατο", "spanish": "La bicicleta", "pronunciation": "Λα μπιθικλέτα"},
                            {"greek": "Αυτοκίνητο", "spanish": "El coche", "pronunciation": "Ελ κότσε"},
                            {"greek": "Στάση", "spanish": "La parada", "pronunciation": "Λα παράδα"},
                            {"greek": "Σταθμός", "spanish": "La estación", "pronunciation": "Λα εσταθιόν"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Πώς Ρωτάμε για Κατεύθυνση",
                        "body": "Μάθε τις βασικές φράσεις για να ρωτήσεις πού βρίσκεται κάτι ή πώς να πας κάπου.",
                        "rules": [
                            "¿Dónde está...? → Πού είναι...;",
                            "¿Cómo llego a...? → Πώς φτάνω στο...;",
                            "Gire a la izquierda. → Στρίψτε αριστερά.",
                            "Gire a la derecha. → Στρίψτε δεξιά.",
                            "Siga recto. → Συνεχίστε ευθεία.",
                            "Está cerca / lejos de aquí. → Είναι κοντά / μακριά από εδώ.",
                            "Tome el autobús número 5. → Πάρτε το λεωφορείο νούμερο 5.",
                            "¿Hay una estación de metro cerca? → Υπάρχει σταθμός μετρό κοντά;",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Διάλογοι Κατεύθυνσης",
                        "examples": [
                            {
                                "spanish": "— Perdone, ¿dónde está la estación de tren?\n— Siga recto y gire a la derecha en la esquina. La estación está al lado del parque.\n— Muchas gracias.\n— De nada.",
                                "greek": "— Συγνώμη, πού είναι ο σταθμός τρένου;\n— Συνεχίστε ευθεία και στρίψτε δεξιά στη γωνία. Ο σταθμός είναι δίπλα στο πάρκο.\n— Ευχαριστώ πολύ.\n— Παρακαλώ.",
                            },
                            {
                                "spanish": "— ¿Cómo llego al museo?\n— Tome el metro, línea 2, y baje en la parada «Sol». El museo está enfrente de la plaza.\n— ¿Está lejos?\n— No, son cinco minutos en metro.",
                                "greek": "— Πώς φτάνω στο μουσείο;\n— Πάρτε το μετρό, γραμμή 2, και κατεβείτε στη στάση «Σολ». Το μουσείο είναι μπροστά από την πλατεία.\n— Είναι μακριά;\n— Όχι, είναι πέντε λεπτά με μετρό.",
                            },
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Χρήσιμες Συμβουλές",
                        "tips": [
                            "Η λέξη «Perdone» (Συγνώμη) ή «Disculpe» (Με συγχωρείτε) είναι ιδανική για να ξεκινήσεις μια ερώτηση σε άγνωστο.",
                            "Στην Ισπανία λένε «coche» για αυτοκίνητο, ενώ στη Λατινική Αμερική λένε «carro» ή «auto».",
                            "Αν δεν καταλαβαίνεις τις οδηγίες, πες: «¿Puede repetir, por favor?» (Μπορείτε να επαναλάβετε, παρακαλώ;).",
                            "Πάντα ξεκίνα τις ερωτήσεις σε ξένους με «usted» (τυπικός τρόπος), όχι «tú».",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Αριστερά» στα Ισπανικά;", "options_json": ["Derecha", "Recto", "Izquierda", "Cerca"], "correct_answer": "Izquierda", "explanation": "Izquierda = Αριστερά", "points": 1},
                {"type": "fill_blank", "prompt": "¿Dónde _____ la estación? (Πού είναι ο σταθμός;)", "options_json": None, "correct_answer": "está", "explanation": "¿Dónde está...? = Πού είναι...;", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «el autobús»;", "options_json": ["Τρένο", "Λεωφορείο", "Μετρό", "Ταξί"], "correct_answer": "Λεωφορείο", "explanation": "El autobús = Λεωφορείο", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «cerca» σημαίνει «μακριά».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Cerca = κοντά, lejos = μακριά.", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Στρίψτε δεξιά» στα Ισπανικά;", "options_json": ["Gire a la izquierda", "Siga recto", "Gire a la derecha", "Tome el metro"], "correct_answer": "Gire a la derecha", "explanation": "Gire a la derecha = Στρίψτε δεξιά", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Πού είναι το μετρό;»", "options_json": None, "correct_answer": "¿Dónde está el metro?", "explanation": "¿Dónde está...? + el metro", "points": 1},
                {"type": "fill_blank", "prompt": "Siga _____ y gire a la izquierda. (Συνεχίστε ευθεία)", "options_json": None, "correct_answer": "recto", "explanation": "Siga recto = Συνεχίστε ευθεία", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «la parada»;", "options_json": ["Σταθμός", "Στάση", "Αεροδρόμιο", "Πλατεία"], "correct_answer": "Στάση", "explanation": "La parada = Στάση", "points": 1},
                {"type": "true_false", "prompt": "Η φράση «¿Cómo llego a...?» σημαίνει «Πόσο κοστίζει;».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "¿Cómo llego a...? = Πώς φτάνω στο...;", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Τρένο» στα Ισπανικά;", "options_json": ["El avión", "El coche", "El tren", "El taxi"], "correct_answer": "El tren", "explanation": "El tren = Τρένο", "points": 1},
                {"type": "fill_blank", "prompt": "Tome el _____ número 5. (Πάρτε το λεωφορείο νούμερο 5)", "options_json": None, "correct_answer": "autobús", "explanation": "Autobús = λεωφορείο", "points": 1},
                {"type": "translation", "prompt": "Μετάφρασε στα Ισπανικά: «Είναι κοντά από εδώ.»", "options_json": None, "correct_answer": "Está cerca de aquí.", "explanation": "Cerca de aquí = κοντά από εδώ", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Κατεύθυνση και Μεταφορά", "passing_score_pct": 60},
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
    print("Seed completed! Chapters 6-10 created with sections, questions and exams.")


if __name__ == "__main__":
    seed()
