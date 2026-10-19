"""
Seed data for chapters, sections, questions, and exams.
Run: python -m app.db.seed_data
"""
from app.db.database import SessionLocal, engine, Base
from app.models.chapter import Chapter
from app.models.section import Section
from app.models.question import Question
from app.models.exam import Exam


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Chapter).count() > 0:
        print("Database already has data. Skipping seed.")
        db.close()
        return

    chapters_data = [
        {
            "order_index": 1,
            "title_greek": "Χαιρετισμοί",
            "title_spanish": "Saludos",
            "difficulty_level": "beginner",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή στους Χαιρετισμούς",
                        "body": "Στο πρώτο κεφάλαιο θα μάθουμε τους βασικούς χαιρετισμούς στα Ισπανικά. Οι χαιρετισμοί είναι το πρώτο βήμα για να ξεκινήσεις μια συνομιλία!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Βασικοί Χαιρετισμοί",
                        "words": [
                            {"greek": "Γεια σου", "spanish": "Hola", "pronunciation": "Όλα"},
                            {"greek": "Καλημέρα", "spanish": "Buenos días", "pronunciation": "Μπουένος ντίας"},
                            {"greek": "Καλησπέρα", "spanish": "Buenas tardes", "pronunciation": "Μπουένας τάρδες"},
                            {"greek": "Καληνύχτα", "spanish": "Buenas noches", "pronunciation": "Μπουένας νότσες"},
                            {"greek": "Αντίο", "spanish": "Adiós", "pronunciation": "Αδιός"},
                            {"greek": "Τα λέμε", "spanish": "Hasta luego", "pronunciation": "Άστα λουέγκο"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "grammar",
                    "content_json": {
                        "title": "Πώς ρωτάμε «Τι κάνεις;»",
                        "body": "Στα Ισπανικά υπάρχουν δύο τρόποι: τυπικός και φιλικός.",
                        "rules": [
                            "¿Cómo estás? (φιλικός) → Πώς είσαι;",
                            "¿Cómo está usted? (τυπικός) → Πώς είστε;",
                            "Estoy bien, gracias. → Είμαι καλά, ευχαριστώ.",
                            "¿Y tú? → Κι εσύ;",
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα Διαλόγων",
                        "examples": [
                            {
                                "spanish": "— ¡Hola! ¿Cómo estás?\n— Estoy bien, gracias. ¿Y tú?\n— Muy bien, gracias.",
                                "greek": "— Γεια σου! Τι κάνεις;\n— Είμαι καλά, ευχαριστώ. Κι εσύ;\n— Πολύ καλά, ευχαριστώ.",
                            },
                            {
                                "spanish": "— Buenos días, señor García.\n— Buenos días. ¿Cómo está usted?\n— Bien, gracias.",
                                "greek": "— Καλημέρα, κύριε Γκαρθία.\n— Καλημέρα. Πώς είστε;\n— Καλά, ευχαριστώ.",
                            },
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "tip",
                    "content_json": {
                        "title": "Χρήσιμες Συμβουλές",
                        "tips": [
                            "Στα Ισπανικά το ερωτηματικό μπαίνει και στην αρχή (ανάποδα ¿) και στο τέλος (;) της ερώτησης!",
                            "Το «usted» χρησιμοποιείται σε επίσημες περιπτώσεις (με αγνώστους, ηλικιωμένους, σε επαγγελματικό πλαίσιο).",
                            "Στην Ισπανία, οι φίλοι χαιρετιούνται συχνά με δύο φιλιά στο μάγουλο!",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Γεια σου» στα Ισπανικά;", "options_json": ["Hola", "Adiós", "Gracias", "Buenos días"], "correct_answer": "Hola", "explanation": "Hola = Γεια σου", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «Buenos días»;", "options_json": ["Καληνύχτα", "Καλημέρα", "Καλησπέρα", "Αντίο"], "correct_answer": "Καλημέρα", "explanation": "Buenos días = Καλημέρα", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Αντίο» στα Ισπανικά;", "options_json": ["Hasta luego", "Hola", "Adiós", "Buenas noches"], "correct_answer": "Adiós", "explanation": "Adiós = Αντίο", "points": 1},
                {"type": "true_false", "prompt": "Η φράση «Buenas tardes» σημαίνει «Καληνύχτα».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Buenas tardes = Καλησπέρα, όχι Καληνύχτα", "points": 1},
                {"type": "true_false", "prompt": "Το «¿Cómo estás?» είναι τυπικός τρόπος να ρωτήσεις «Τι κάνεις;».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Είναι φιλικός τρόπος. Ο τυπικός είναι «¿Cómo está usted?»", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «Hasta luego»;", "options_json": ["Καλημέρα", "Γεια σου", "Τα λέμε", "Ευχαριστώ"], "correct_answer": "Τα λέμε", "explanation": "Hasta luego = Τα λέμε", "points": 1},
                {"type": "fill_blank", "prompt": "Συμπλήρωσε: «¿Cómo _____?» (Τι κάνεις; - φιλικά)", "options_json": None, "correct_answer": "estás", "explanation": "¿Cómo estás? = Τι κάνεις; (φιλικά)", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια φράση χρησιμοποιούμε το βράδυ;", "options_json": ["Buenos días", "Buenas tardes", "Buenas noches", "Hasta luego"], "correct_answer": "Buenas noches", "explanation": "Buenas noches = Καληνύχτα (χρησιμοποιείται το βράδυ)", "points": 1},
                {"type": "true_false", "prompt": "Στα Ισπανικά, το ερωτηματικό μπαίνει μόνο στο τέλος της πρότασης.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Μπαίνει και στην αρχή (¿) και στο τέλος (?)", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς απαντάμε στο «¿Cómo estás?»;", "options_json": ["Adiós", "Estoy bien, gracias", "Hasta luego", "Buenos días"], "correct_answer": "Estoy bien, gracias", "explanation": "Estoy bien, gracias = Είμαι καλά, ευχαριστώ", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Χαιρετισμοί", "passing_score_pct": 60},
        },
        {
            "order_index": 2,
            "title_greek": "Αριθμοί 1-20",
            "title_spanish": "Números 1-20",
            "difficulty_level": "beginner",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Εισαγωγή στους Αριθμούς",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις να μετράς από το 1 μέχρι το 20 στα Ισπανικά. Οι αριθμοί είναι απαραίτητοι στην καθημερινή ζωή!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "video",
                    "content_json": {
                        "title": "Βίντεο: Αριθμοί 1-20",
                        "youtube_url": "https://www.youtube.com/watch?v=C58QilFeKow",
                        "description": "Δες και άκουσε τους αριθμούς από το 1 μέχρι το 20 στα Ισπανικά πριν συνεχίσεις με το λεξιλόγιο.",
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Αριθμοί 1-10",
                        "words": [
                            {"greek": "1 - Ένα", "spanish": "Uno", "pronunciation": "Ούνο"},
                            {"greek": "2 - Δύο", "spanish": "Dos", "pronunciation": "Ντος"},
                            {"greek": "3 - Τρία", "spanish": "Tres", "pronunciation": "Τρες"},
                            {"greek": "4 - Τέσσερα", "spanish": "Cuatro", "pronunciation": "Κουάτρο"},
                            {"greek": "5 - Πέντε", "spanish": "Cinco", "pronunciation": "Θίνκο"},
                            {"greek": "6 - Έξι", "spanish": "Seis", "pronunciation": "Σέις"},
                            {"greek": "7 - Εφτά", "spanish": "Siete", "pronunciation": "Σιέτε"},
                            {"greek": "8 - Οχτώ", "spanish": "Ocho", "pronunciation": "Ότσο"},
                            {"greek": "9 - Εννιά", "spanish": "Nueve", "pronunciation": "Νουέβε"},
                            {"greek": "10 - Δέκα", "spanish": "Diez", "pronunciation": "Ντιέθ"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "vocab",
                    "content_json": {
                        "title": "Αριθμοί 11-20",
                        "words": [
                            {"greek": "11 - Έντεκα", "spanish": "Once", "pronunciation": "Όνθε"},
                            {"greek": "12 - Δώδεκα", "spanish": "Doce", "pronunciation": "Ντόθε"},
                            {"greek": "13 - Δεκατρία", "spanish": "Trece", "pronunciation": "Τρέθε"},
                            {"greek": "14 - Δεκατέσσερα", "spanish": "Catorce", "pronunciation": "Κατόρθε"},
                            {"greek": "15 - Δεκαπέντε", "spanish": "Quince", "pronunciation": "Κίνθε"},
                            {"greek": "16 - Δεκαέξι", "spanish": "Dieciséis", "pronunciation": "Ντιεθισέις"},
                            {"greek": "17 - Δεκαεφτά", "spanish": "Diecisiete", "pronunciation": "Ντιεθισιέτε"},
                            {"greek": "18 - Δεκαοχτώ", "spanish": "Dieciocho", "pronunciation": "Ντιεθιότσο"},
                            {"greek": "19 - Δεκαεννιά", "spanish": "Diecinueve", "pronunciation": "Ντιεθινουέβε"},
                            {"greek": "20 - Είκοσι", "spanish": "Veinte", "pronunciation": "Βέιντε"},
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "grammar",
                    "content_json": {
                        "title": "Χρήσιμες Εκφράσεις με Αριθμούς",
                        "body": "Μάθε πώς να χρησιμοποιείς τους αριθμούς σε καθημερινές καταστάσεις.",
                        "rules": [
                            "¿Cuántos años tienes? → Πόσα χρόνια είσαι; (Πόσο χρονών είσαι;)",
                            "Tengo veinte años. → Είμαι είκοσι χρονών.",
                            "¿Cuánto cuesta? → Πόσο κοστίζει;",
                            "Son cinco euros. → Είναι πέντε ευρώ.",
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "tip",
                    "content_json": {
                        "title": "Συμβουλές Αποστήθισης",
                        "tips": [
                            "Οι αριθμοί 1-15 έχουν μοναδική μορφή — πρέπει να τους αποστηθίσεις.",
                            "Οι αριθμοί 16-19 σχηματίζονται: dieci + αριθμός (π.χ. dieci+seis = dieciséis).",
                            "Προσπάθησε να μετράς αντικείμενα γύρω σου στα Ισπανικά!",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "fill_blank", "prompt": "Πώς λέμε το 5 στα Ισπανικά; _____", "options_json": None, "correct_answer": "cinco", "explanation": "5 = cinco", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι αριθμό αντιστοιχεί το «doce»;", "options_json": ["10", "11", "12", "13"], "correct_answer": "12", "explanation": "Doce = 12", "points": 1},
                {"type": "fill_blank", "prompt": "Συμπλήρωσε: Uno, dos, _____, cuatro", "options_json": None, "correct_answer": "tres", "explanation": "1, 2, 3, 4 → tres = 3", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε το «15» στα Ισπανικά;", "options_json": ["Catorce", "Quince", "Dieciséis", "Trece"], "correct_answer": "Quince", "explanation": "15 = Quince", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιος αριθμός είναι το «siete»;", "options_json": ["6", "7", "8", "9"], "correct_answer": "7", "explanation": "Siete = 7", "points": 1},
                {"type": "fill_blank", "prompt": "Πώς λέμε «20» στα Ισπανικά; _____", "options_json": None, "correct_answer": "veinte", "explanation": "20 = veinte", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «dieciocho»;", "options_json": ["16", "17", "18", "19"], "correct_answer": "18", "explanation": "Dieciocho = 18", "points": 1},
                {"type": "fill_blank", "prompt": "Ocho + dos = _____", "options_json": None, "correct_answer": "diez", "explanation": "8 + 2 = 10 = diez", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Πόσο χρονών είσαι;» στα Ισπανικά;", "options_json": ["¿Cómo estás?", "¿Cuántos años tienes?", "¿Cuánto cuesta?", "¿Cómo te llamas?"], "correct_answer": "¿Cuántos años tienes?", "explanation": "¿Cuántos años tienes? = Πόσο χρονών είσαι;", "points": 1},
                {"type": "fill_blank", "prompt": "Diez + uno = _____", "options_json": None, "correct_answer": "once", "explanation": "10 + 1 = 11 = once", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Αριθμοί 1-20", "passing_score_pct": 60},
        },
        {
            "order_index": 3,
            "title_greek": "Χρώματα και Αντικείμενα",
            "title_spanish": "Colores y Objetos",
            "difficulty_level": "beginner",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Χρώματα & Αντικείμενα",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις τα βασικά χρώματα και κοινά αντικείμενα. Θα δεις επίσης πώς τα χρώματα αλλάζουν ανάλογα με το γένος του ουσιαστικού!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "vocab",
                    "content_json": {
                        "title": "Τα Χρώματα",
                        "words": [
                            {"greek": "Κόκκινο", "spanish": "Rojo/Roja", "pronunciation": "Ρόχο/Ρόχα"},
                            {"greek": "Μπλε", "spanish": "Azul", "pronunciation": "Αθούλ"},
                            {"greek": "Πράσινο", "spanish": "Verde", "pronunciation": "Βέρντε"},
                            {"greek": "Κίτρινο", "spanish": "Amarillo/Amarilla", "pronunciation": "Αμαρίγιο/Αμαρίγια"},
                            {"greek": "Μαύρο", "spanish": "Negro/Negra", "pronunciation": "Νέγκρο/Νέγκρα"},
                            {"greek": "Λευκό", "spanish": "Blanco/Blanca", "pronunciation": "Μπλάνκο/Μπλάνκα"},
                        ],
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Κοινά Αντικείμενα",
                        "words": [
                            {"greek": "Βιβλίο", "spanish": "El libro", "pronunciation": "Ελ λίμπρο"},
                            {"greek": "Τραπέζι", "spanish": "La mesa", "pronunciation": "Λα μέσα"},
                            {"greek": "Καρέκλα", "spanish": "La silla", "pronunciation": "Λα σίγια"},
                            {"greek": "Στυλό", "spanish": "El bolígrafo", "pronunciation": "Ελ μπολίγραφο"},
                            {"greek": "Τετράδιο", "spanish": "El cuaderno", "pronunciation": "Ελ κουαδέρνο"},
                            {"greek": "Πόρτα", "spanish": "La puerta", "pronunciation": "Λα πουέρτα"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Γένος και Χρώματα",
                        "body": "Στα Ισπανικά τα επίθετα (όπως τα χρώματα) πρέπει να συμφωνούν σε γένος με το ουσιαστικό.",
                        "rules": [
                            "El libro rojo (Το κόκκινο βιβλίο) — αρσενικό → rojo",
                            "La mesa roja (Το κόκκινο τραπέζι) — θηλυκό → roja",
                            "Τα χρώματα που τελειώνουν σε -e (verde) ή σε σύμφωνο (azul) δεν αλλάζουν!",
                            "El libro verde / La mesa verde → το ίδιο!",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "tip",
                    "content_json": {
                        "title": "Μνημονικά Κόλπα",
                        "tips": [
                            "El = αρσενικό άρθρο, La = θηλυκό άρθρο — αντίστοιχα του ο/η στα Ελληνικά.",
                            "Τα ουσιαστικά που τελειώνουν σε -o είναι συνήθως αρσενικά, σε -a θηλυκά.",
                            "Δοκίμασε να κοιτάξεις γύρω σου και να πεις τα χρώματα των αντικειμένων στα Ισπανικά!",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Κόκκινο» στα Ισπανικά (αρσενικό);", "options_json": ["Verde", "Rojo", "Azul", "Negro"], "correct_answer": "Rojo", "explanation": "Rojo = Κόκκινο (αρσ.)", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «La mesa»;", "options_json": ["Η καρέκλα", "Το βιβλίο", "Το τραπέζι", "Η πόρτα"], "correct_answer": "Το τραπέζι", "explanation": "La mesa = Το τραπέζι", "points": 1},
                {"type": "fill_blank", "prompt": "Συμπλήρωσε: La silla _____ (μπλε)", "options_json": None, "correct_answer": "azul", "explanation": "Azul δεν αλλάζει γένος", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο είναι το σωστό; «Το κόκκινο βιβλίο»", "options_json": ["El libro roja", "El libro rojo", "La libro rojo", "El libra rojo"], "correct_answer": "El libro rojo", "explanation": "Libro = αρσενικό → rojo", "points": 1},
                {"type": "true_false", "prompt": "Το χρώμα «verde» αλλάζει μορφή ανάλογα με το γένος.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Τα χρώματα σε -e δεν αλλάζουν", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Η καρέκλα» στα Ισπανικά;", "options_json": ["El silla", "La silla", "El libro", "La mesa"], "correct_answer": "La silla", "explanation": "La silla = Η καρέκλα", "points": 1},
                {"type": "fill_blank", "prompt": "El cuaderno _____ (μαύρο)", "options_json": None, "correct_answer": "negro", "explanation": "Cuaderno = αρσενικό → negro", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο άρθρο χρησιμοποιούμε για αρσενικά ουσιαστικά;", "options_json": ["La", "El", "Los", "Un"], "correct_answer": "El", "explanation": "El = αρσενικό οριστικό άρθρο", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «puerta» είναι αρσενικού γένους.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "La puerta = θηλυκό", "points": 1},
                {"type": "multiple_choice", "prompt": "«La mesa blanca» σημαίνει:", "options_json": ["Το μαύρο τραπέζι", "Η λευκή καρέκλα", "Το λευκό τραπέζι", "Το μπλε τραπέζι"], "correct_answer": "Το λευκό τραπέζι", "explanation": "Mesa = τραπέζι, blanca = λευκή", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Χρώματα και Αντικείμενα", "passing_score_pct": 60},
        },
        {
            "order_index": 4,
            "title_greek": "Η Οικογένεια",
            "title_spanish": "La Familia",
            "difficulty_level": "beginner",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Η Οικογένεια στα Ισπανικά",
                        "body": "Σε αυτό το κεφάλαιο θα μάθεις τα μέλη της οικογένειας και τις κτητικές αντωνυμίες (mi, tu, su).",
                    },
                },
                {
                    "order_index": 2,
                    "type": "video",
                    "content_json": {
                        "title": "Βίντεο: Η Οικογένεια",
                        "youtube_url": "https://www.youtube.com/watch?v=3Odc-nGvKzM",
                        "description": "Δες και άκουσε τα μέλη της οικογένειας στα Ισπανικά πριν συνεχίσεις με το λεξιλόγιο.",
                    },
                },
                {
                    "order_index": 3,
                    "type": "vocab",
                    "content_json": {
                        "title": "Μέλη της Οικογένειας",
                        "words": [
                            {"greek": "Μητέρα", "spanish": "La madre", "pronunciation": "Λα μάδρε"},
                            {"greek": "Πατέρας", "spanish": "El padre", "pronunciation": "Ελ πάδρε"},
                            {"greek": "Αδερφός", "spanish": "El hermano", "pronunciation": "Ελ ερμάνο"},
                            {"greek": "Αδερφή", "spanish": "La hermana", "pronunciation": "Λα ερμάνα"},
                            {"greek": "Παππούς", "spanish": "El abuelo", "pronunciation": "Ελ αμπουέλο"},
                            {"greek": "Γιαγιά", "spanish": "La abuela", "pronunciation": "Λα αμπουέλα"},
                            {"greek": "Γιος", "spanish": "El hijo", "pronunciation": "Ελ ίχο"},
                            {"greek": "Κόρη", "spanish": "La hija", "pronunciation": "Λα ίχα"},
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κτητικές Αντωνυμίες",
                        "body": "Χρησιμοποιούμε κτητικές αντωνυμίες για να δείξουμε σε ποιον ανήκει κάτι.",
                        "rules": [
                            "Mi = Μου (mi madre = η μητέρα μου)",
                            "Tu = Σου (tu hermano = ο αδερφός σου)",
                            "Su = Του/Της/Σας (su padre = ο πατέρας του/της)",
                            "Mis = Μου (πληθ.) (mis hermanos = τα αδέρφια μου)",
                            "Tus = Σου (πληθ.) (tus abuelos = οι παππούδες σου)",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα",
                        "examples": [
                            {"spanish": "Mi madre se llama María.", "greek": "Η μητέρα μου λέγεται Μαρία."},
                            {"spanish": "¿Cuántos hermanos tienes?", "greek": "Πόσα αδέρφια έχεις;"},
                            {"spanish": "Tengo dos hermanas y un hermano.", "greek": "Έχω δύο αδερφές και έναν αδερφό."},
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Πώς λέμε «Μητέρα» στα Ισπανικά;", "options_json": ["La hermana", "La madre", "La abuela", "La hija"], "correct_answer": "La madre", "explanation": "La madre = Μητέρα", "points": 1},
                {"type": "fill_blank", "prompt": "_____ madre se llama Ana. (η μητέρα μου)", "options_json": None, "correct_answer": "Mi", "explanation": "Mi = μου", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «el abuelo»;", "options_json": ["Ο πατέρας", "Ο αδερφός", "Ο παππούς", "Ο γιος"], "correct_answer": "Ο παππούς", "explanation": "El abuelo = Ο παππούς", "points": 1},
                {"type": "true_false", "prompt": "Η λέξη «hermana» σημαίνει «αδερφός».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Hermana = αδερφή, hermano = αδερφός", "points": 1},
                {"type": "multiple_choice", "prompt": "Πώς λέμε «τα αδέρφια σου» (πληθ.);", "options_json": ["Mi hermanos", "Tu hermano", "Tus hermanos", "Su hermana"], "correct_answer": "Tus hermanos", "explanation": "Tus = σου (πληθ.), hermanos = αδέρφια", "points": 1},
                {"type": "fill_blank", "prompt": "El _____ es el padre de mi padre. (παππούς)", "options_json": None, "correct_answer": "abuelo", "explanation": "El abuelo = ο παππούς", "points": 1},
                {"type": "multiple_choice", "prompt": "Τι σημαίνει «la hija»;", "options_json": ["Η μητέρα", "Η αδερφή", "Η κόρη", "Η γιαγιά"], "correct_answer": "Η κόρη", "explanation": "La hija = Η κόρη", "points": 1},
                {"type": "true_false", "prompt": "Η κτητική αντωνυμία «su» μπορεί να σημαίνει «του», «της» ή «σας».", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Σωστό", "explanation": "Su = του/της/σας", "points": 1},
                {"type": "fill_blank", "prompt": "Tengo dos _____. (αδερφές)", "options_json": None, "correct_answer": "hermanas", "explanation": "Hermanas = αδερφές", "points": 1},
                {"type": "multiple_choice", "prompt": "«Mi padre» σημαίνει:", "options_json": ["Ο πατέρας σου", "Ο πατέρας μου", "Ο παππούς μου", "Ο αδερφός μου"], "correct_answer": "Ο πατέρας μου", "explanation": "Mi padre = Ο πατέρας μου", "points": 1},
            ],
            "exam": {"title": "Εξέταση: Η Οικογένεια", "passing_score_pct": 60},
        },
        {
            "order_index": 5,
            "title_greek": "Ρήμα SER & ESTAR",
            "title_spanish": "Verbos SER y ESTAR",
            "difficulty_level": "beginner",
            "sections": [
                {
                    "order_index": 1,
                    "type": "text",
                    "content_json": {
                        "title": "Τα δύο «είμαι» στα Ισπανικά",
                        "body": "Στα Ισπανικά υπάρχουν δύο ρήματα που σημαίνουν «είμαι»: SER και ESTAR. Αυτό είναι ένα από τα πιο σημαντικά θέματα στα Ισπανικά!",
                    },
                },
                {
                    "order_index": 2,
                    "type": "video",
                    "content_json": {
                        "title": "Βίντεο: SER & ESTAR",
                        "youtube_url": "https://www.youtube.com/watch?v=gZCueT89J6E",
                        "description": "Δες την εξήγηση για τη διαφορά μεταξύ SER και ESTAR πριν συνεχίσεις με την κλίση και τους κανόνες.",
                    },
                },
                {
                    "order_index": 3,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση του SER",
                        "body": "Το SER χρησιμοποιείται για μόνιμα χαρακτηριστικά.",
                        "rules": [
                            "Yo soy → Εγώ είμαι",
                            "Tú eres → Εσύ είσαι",
                            "Él/Ella es → Αυτός/Αυτή είναι",
                            "Nosotros somos → Εμείς είμαστε",
                            "Vosotros sois → Εσείς είστε",
                            "Ellos/Ellas son → Αυτοί/Αυτές είναι",
                        ],
                    },
                },
                {
                    "order_index": 4,
                    "type": "grammar",
                    "content_json": {
                        "title": "Κλίση του ESTAR",
                        "body": "Το ESTAR χρησιμοποιείται για προσωρινές καταστάσεις και τοποθεσία.",
                        "rules": [
                            "Yo estoy → Εγώ είμαι",
                            "Tú estás → Εσύ είσαι",
                            "Él/Ella está → Αυτός/Αυτή είναι",
                            "Nosotros estamos → Εμείς είμαστε",
                            "Vosotros estáis → Εσείς είστε",
                            "Ellos/Ellas están → Αυτοί/Αυτές είναι",
                        ],
                    },
                },
                {
                    "order_index": 5,
                    "type": "grammar",
                    "content_json": {
                        "title": "Πότε SER vs ESTAR;",
                        "body": "Αυτός είναι ο πιο σημαντικός κανόνας αυτού του κεφαλαίου.",
                        "rules": [
                            "SER → Εθνικότητα: Soy griego. (Είμαι Έλληνας)",
                            "SER → Επάγγελμα: Ella es profesora. (Είναι δασκάλα)",
                            "SER → Μόνιμα χαρακτηριστικά: Es alto. (Είναι ψηλός)",
                            "SER → Ώρα/Ημ/νια: Son las tres. (Είναι τρεις η ώρα)",
                            "ESTAR → Τοποθεσία: Estoy en casa. (Είμαι στο σπίτι)",
                            "ESTAR → Συναισθήματα: Estoy contento. (Είμαι χαρούμενος)",
                            "ESTAR → Υγεία: Estoy enfermo. (Είμαι άρρωστος)",
                            "ESTAR → Προσωρινό: La comida está fría. (Το φαγητό είναι κρύο)",
                        ],
                    },
                },
                {
                    "order_index": 6,
                    "type": "example",
                    "content_json": {
                        "title": "Παραδείγματα",
                        "examples": [
                            {"spanish": "Yo soy estudiante.", "greek": "Εγώ είμαι φοιτητής. (SER — μόνιμο)"},
                            {"spanish": "Yo estoy cansado.", "greek": "Εγώ είμαι κουρασμένος. (ESTAR — προσωρινό)"},
                            {"spanish": "Madrid es la capital de España.", "greek": "Η Μαδρίτη είναι η πρωτεύουσα της Ισπανίας. (SER — μόνιμο)"},
                            {"spanish": "Mi hermano está en Madrid.", "greek": "Ο αδερφός μου είναι στη Μαδρίτη. (ESTAR — τοποθεσία)"},
                        ],
                    },
                },
                {
                    "order_index": 7,
                    "type": "tip",
                    "content_json": {
                        "title": "Κόλπο Μνήμης",
                        "tips": [
                            "SER = ΑΥΤΟ ΠΟΥ ΕΙΣΑΙ (ταυτότητα, φύση)",
                            "ESTAR = ΠΩΣ/ΠΟΥ ΕΙΣΑΙ (κατάσταση, τοποθεσία)",
                            "Σκέψου: Soy griego (δεν αλλάζει) vs Estoy contento (μπορεί να αλλάξει)",
                        ],
                    },
                },
            ],
            "questions": [
                {"type": "multiple_choice", "prompt": "Ποιο ρήμα χρησιμοποιούμε για εθνικότητα;", "options_json": ["Estar", "Ser", "Tener", "Ir"], "correct_answer": "Ser", "explanation": "Soy griego → SER για μόνιμα", "points": 1},
                {"type": "fill_blank", "prompt": "Yo _____ estudiante. (Είμαι φοιτητής)", "options_json": None, "correct_answer": "soy", "explanation": "Soy = είμαι (SER, 1ο πρόσωπο)", "points": 1},
                {"type": "fill_blank", "prompt": "Ella _____ en casa. (Είναι στο σπίτι)", "options_json": None, "correct_answer": "está", "explanation": "Está = είναι (ESTAR, τοποθεσία)", "points": 1},
                {"type": "true_false", "prompt": "Χρησιμοποιούμε ESTAR για να πούμε την ώρα.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Χρησιμοποιούμε SER: Son las tres.", "points": 1},
                {"type": "multiple_choice", "prompt": "«Estoy cansado» σημαίνει:", "options_json": ["Είμαι Ισπανός", "Είμαι ψηλός", "Είμαι κουρασμένος", "Είμαι δάσκαλος"], "correct_answer": "Είμαι κουρασμένος", "explanation": "ESTAR + κουρασμένος = προσωρινή κατάσταση", "points": 1},
                {"type": "fill_blank", "prompt": "Nosotros _____ griegos. (Είμαστε Έλληνες)", "options_json": None, "correct_answer": "somos", "explanation": "Somos = είμαστε (SER)", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποια είναι η σωστή πρόταση;", "options_json": ["Ella es enferma", "Ella está enferma", "Ella está profesora", "Ella es en casa"], "correct_answer": "Ella está enferma", "explanation": "Αρρώστια = προσωρινό → ESTAR", "points": 1},
                {"type": "fill_blank", "prompt": "Tú _____ muy inteligente. (Εσύ είσαι πολύ έξυπνος — μόνιμο)", "options_json": None, "correct_answer": "eres", "explanation": "Eres = είσαι (SER, μόνιμο χαρακτηριστικό)", "points": 1},
                {"type": "true_false", "prompt": "Η πρόταση «Estoy griego» είναι σωστή.", "options_json": ["Σωστό", "Λάθος"], "correct_answer": "Λάθος", "explanation": "Εθνικότητα → SER: Soy griego", "points": 1},
                {"type": "multiple_choice", "prompt": "«Ellos son» σημαίνει:", "options_json": ["Αυτοί είναι (SER)", "Αυτοί είναι (ESTAR)", "Εμείς είμαστε", "Εσείς είστε"], "correct_answer": "Αυτοί είναι (SER)", "explanation": "Son = είναι (SER, 3ο πληθ.)", "points": 1},
                {"type": "fill_blank", "prompt": "La comida _____ fría. (Το φαγητό είναι κρύο)", "options_json": None, "correct_answer": "está", "explanation": "Προσωρινή κατάσταση → ESTAR", "points": 1},
                {"type": "multiple_choice", "prompt": "Ποιο είναι σωστό; «Η Μαδρίτη είναι στην Ισπανία»", "options_json": ["Madrid ser en España", "Madrid está en España", "Madrid es en España", "Madrid estoy en España"], "correct_answer": "Madrid está en España", "explanation": "Τοποθεσία → ESTAR: Madrid está en España", "points": 1},
            ],
            "exam": {"title": "Εξέταση: SER & ESTAR", "passing_score_pct": 60},
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
    print("Seed completed! 5 chapters created with sections, questions and exams.")


if __name__ == "__main__":
    seed()
