import io
import logging

from gtts import gTTS

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


# =========================================================
# UNKNOWN WORLD AI
# FULL LANGUAGE LEARNING SYSTEM + VOICE
# =========================================================

LANGUAGES = {
    "english": {
        "name": "🇬🇧 English",
        "native": "English",
        "tts": "en",
    },
    "german": {
        "name": "🇩🇪 German",
        "native": "Deutsch",
        "tts": "de",
    },
    "swedish": {
        "name": "🇸🇪 Swedish",
        "native": "Svenska",
        "tts": "sv",
    },
    "thai": {
        "name": "🇹🇭 Thai",
        "native": "ภาษาไทย",
        "tts": "th",
    },
    "chinese": {
        "name": "🇨🇳 Chinese",
        "native": "中文",
        "tts": "zh-CN",
    },
    "spanish": {
        "name": "🇪🇸 Spanish",
        "native": "Español",
        "tts": "es",
    },
}


LEVELS = {
    "beginner": "🟢 Beginner",
    "intermediate": "🟡 Intermediate",
    "advanced": "🔴 Advanced",
}


# =========================================================
# LESSON DATABASE
# =========================================================

LESSONS = {

    # =====================================================
    # ENGLISH
    # =====================================================

    "english": {

        "beginner": [

            {
                "title": "Introducing Yourself",
                "word": "Hello",
                "meaning": "مرحبا",
                "pronunciation": "هِلّو",
                "sentence": "Hello, my name is Ali.",
                "translation": "مرحباً، اسمي علي.",
                "explanation": "Use Hello when greeting someone.",
                "grammar": "My name is + name.",
                "question": "What is your name?",
                "options": [
                    "My name is Ali.",
                    "I am from yesterday.",
                    "Good night is blue."
                ],
                "answer": "My name is Ali.",
            },

            {
                "title": "Where Are You From?",
                "word": "From",
                "meaning": "من",
                "pronunciation": "فرَم",
                "sentence": "I am from Sweden.",
                "translation": "أنا من السويد.",
                "explanation": "Use 'from' to talk about origin.",
                "grammar": "I am from + country/city.",
                "question": "Where are you from?",
                "options": [
                    "I am from Sweden.",
                    "I am eating Sweden.",
                    "Sweden is yesterday."
                ],
                "answer": "I am from Sweden.",
            },

            {
                "title": "Daily Learning",
                "word": "Learn",
                "meaning": "يتعلم",
                "pronunciation": "لِرن",
                "sentence": "I am learning English every day.",
                "translation": "أنا أتعلم الإنجليزية كل يوم.",
                "explanation": "Learning means gaining knowledge or a skill.",
                "grammar": "I am + verb-ing.",
                "question": "What are you learning?",
                "options": [
                    "I am learning English.",
                    "I am English learning yesterday.",
                    "Learning is blue."
                ],
                "answer": "I am learning English.",
            },

            {
                "title": "Everyday Questions",
                "word": "How",
                "meaning": "كيف",
                "pronunciation": "هاو",
                "sentence": "How are you?",
                "translation": "كيف حالك؟",
                "explanation": "How is commonly used to ask about condition or method.",
                "grammar": "How + be + subject?",
                "question": "How are you?",
                "options": [
                    "I am fine, thank you.",
                    "I am from Sweden.",
                    "My name is Ali."
                ],
                "answer": "I am fine, thank you.",
            },

            {
                "title": "Work",
                "word": "Work",
                "meaning": "عمل",
                "pronunciation": "وِرك",
                "sentence": "I work in a restaurant.",
                "translation": "أنا أعمل في مطعم.",
                "explanation": "Work can be used as a noun or verb.",
                "grammar": "I work + place.",
                "question": "Where do you work?",
                "options": [
                    "I work in a restaurant.",
                    "I restaurant yesterday.",
                    "Work is green."
                ],
                "answer": "I work in a restaurant.",
            },

            {
                "title": "Food",
                "word": "Food",
                "meaning": "طعام",
                "pronunciation": "فود",
                "sentence": "I like good food.",
                "translation": "أنا أحب الطعام الجيد.",
                "explanation": "Food means things that people eat.",
                "grammar": "I like + noun.",
                "question": "What do you like?",
                "options": [
                    "I like good food.",
                    "I like yesterday.",
                    "Food am good."
                ],
                "answer": "I like good food.",
            },

            {
                "title": "Time",
                "word": "Today",
                "meaning": "اليوم",
                "pronunciation": "تُداي",
                "sentence": "I am busy today.",
                "translation": "أنا مشغول اليوم.",
                "explanation": "Today means this current day.",
                "grammar": "Subject + be + adjective + today.",
                "question": "Are you busy today?",
                "options": [
                    "Yes, I am busy today.",
                    "Yes, I am Sweden.",
                    "Today is a person."
                ],
                "answer": "Yes, I am busy today.",
            },

            {
                "title": "Future Plans",
                "word": "Tomorrow",
                "meaning": "غداً",
                "pronunciation": "تُمارو",
                "sentence": "I will study tomorrow.",
                "translation": "سأدرس غداً.",
                "explanation": "Will can describe future actions.",
                "grammar": "I will + verb.",
                "question": "What will you do tomorrow?",
                "options": [
                    "I will study tomorrow.",
                    "I studied tomorrow yesterday.",
                    "Tomorrow is food."
                ],
                "answer": "I will study tomorrow.",
            },

            {
                "title": "Review",
                "word": "Practice",
                "meaning": "ممارسة",
                "pronunciation": "براكتِس",
                "sentence": "I practice English every day.",
                "translation": "أمارس الإنجليزية كل يوم.",
                "explanation": "Practice helps improve a language skill.",
                "grammar": "I practice + language/skill.",
                "question": "How often do you practice?",
                "options": [
                    "Every day.",
                    "Yesterday is blue.",
                    "I am Sweden."
                ],
                "answer": "Every day.",
            },
        ],

        "intermediate": [

            {
                "title": "Conversation",
                "word": "Conversation",
                "meaning": "محادثة",
                "pronunciation": "كونڤرسيشن",
                "sentence": "I want to have a conversation in English.",
                "translation": "أريد أن أجري محادثة بالإنجليزية.",
                "explanation": "Conversation means talking with another person.",
                "grammar": "I want to + verb.",
                "question": "What do you want to do?",
                "options": [
                    "I want to have a conversation.",
                    "I want conversation yesterday.",
                    "I am conversation."
                ],
                "answer": "I want to have a conversation.",
            },

            {
                "title": "Experience",
                "word": "Experience",
                "meaning": "خبرة / تجربة",
                "pronunciation": "إكسبيرينس",
                "sentence": "I have experience working with customers.",
                "translation": "لدي خبرة في التعامل مع الزبائن.",
                "explanation": "Experience can describe knowledge gained from work or life.",
                "grammar": "I have + noun.",
                "question": "Do you have work experience?",
                "options": [
                    "Yes, I have some experience.",
                    "Experience is yesterday.",
                    "I am experience."
                ],
                "answer": "Yes, I have some experience.",
            },

            {
                "title": "Plans",
                "word": "Plan",
                "meaning": "خطة",
                "pronunciation": "بلان",
                "sentence": "I am planning my future.",
                "translation": "أنا أخطط لمستقبلي.",
                "explanation": "Plan means deciding what you want to do.",
                "grammar": "I am planning + object.",
                "question": "What are you planning?",
                "options": [
                    "I am planning my future.",
                    "I planning yesterday.",
                    "Future am plan."
                ],
                "answer": "I am planning my future.",
            },
        ],

        "advanced": [

            {
                "title": "Fluent Communication",
                "word": "Communicate",
                "meaning": "يتواصل",
                "pronunciation": "كميونيكيت",
                "sentence": "I want to communicate clearly and confidently.",
                "translation": "أريد أن أتواصل بوضوح وثقة.",
                "explanation": "Clear communication means expressing ideas so other people understand them.",
                "grammar": "want to + verb.",
                "question": "How do you want to communicate?",
                "options": [
                    "Clearly and confidently.",
                    "Yesterday and blue.",
                    "By eating."
                ],
                "answer": "Clearly and confidently.",
            },
        ],
    },


    # =====================================================
    # GERMAN
    # =====================================================

    "german": {

        "beginner": [

            {
                "title": "Greeting",
                "word": "Hallo",
                "meaning": "مرحبا",
                "pronunciation": "هالو",
                "sentence": "Hallo, ich heiße Ali.",
                "translation": "مرحباً، اسمي علي.",
                "explanation": "Hallo means hello.",
                "grammar": "Ich heiße + Name.",
                "question": "Wie heißt du?",
                "options": [
                    "Ich heiße Ali.",
                    "Ich bin gestern.",
                    "Ali ist blau."
                ],
                "answer": "Ich heiße Ali.",
            },

            {
                "title": "Origin",
                "word": "Aus",
                "meaning": "من",
                "pronunciation": "آوس",
                "sentence": "Ich komme aus Schweden.",
                "translation": "أنا من السويد.",
                "explanation": "Aus is used to express origin.",
                "grammar": "Ich komme aus + Land.",
                "question": "Woher kommst du?",
                "options": [
                    "Ich komme aus Schweden.",
                    "Ich esse Schweden.",
                    "Schweden ist morgen."
                ],
                "answer": "Ich komme aus Schweden.",
            },

            {
                "title": "Learning",
                "word": "Lernen",
                "meaning": "يتعلم",
                "pronunciation": "ليرنن",
                "sentence": "Ich lerne Deutsch.",
                "translation": "أنا أتعلم الألمانية.",
                "explanation": "Lernen means to learn.",
                "grammar": "Ich lerne + subject.",
                "question": "Was lernst du?",
                "options": [
                    "Ich lerne Deutsch.",
                    "Deutsch ist gestern.",
                    "Ich Deutsch blau."
                ],
                "answer": "Ich lerne Deutsch.",
            },

            {
                "title": "Work",
                "word": "Arbeiten",
                "meaning": "يعمل",
                "pronunciation": "أربايتن",
                "sentence": "Ich arbeite in einem Restaurant.",
                "translation": "أنا أعمل في مطعم.",
                "explanation": "Arbeiten means to work.",
                "grammar": "Ich arbeite in + place.",
                "question": "Wo arbeitest du?",
                "options": [
                    "Ich arbeite in einem Restaurant.",
                    "Ich Restaurant morgen.",
                    "Arbeiten ist Essen."
                ],
                "answer": "Ich arbeite in einem Restaurant.",
            },

            {
                "title": "Thank You",
                "word": "Danke",
                "meaning": "شكراً",
                "pronunciation": "دانكه",
                "sentence": "Danke schön.",
                "translation": "شكراً جزيلاً.",
                "explanation": "Danke means thank you.",
                "grammar": "Danke + adjective.",
                "question": "How do you say thank you?",
                "options": [
                    "Danke schön.",
                    "Guten Morgen means food.",
                    "Hallo gestern."
                ],
                "answer": "Danke schön.",
            },
        ],

        "intermediate": [

            {
                "title": "Daily Life",
                "word": "Alltag",
                "meaning": "الحياة اليومية",
                "pronunciation": "ألتاغ",
                "sentence": "Mein Alltag ist manchmal sehr beschäftigt.",
                "translation": "حياتي اليومية تكون مشغولة أحياناً.",
                "explanation": "Alltag means everyday life.",
                "grammar": "Mein + noun + ist + adjective.",
                "question": "Wie ist dein Alltag?",
                "options": [
                    "Mein Alltag ist beschäftigt.",
                    "Mein Alltag essen.",
                    "Alltag ist gestern."
                ],
                "answer": "Mein Alltag ist beschäftigt.",
            },

            {
                "title": "Future",
                "word": "Zukunft",
                "meaning": "المستقبل",
                "pronunciation": "تسوكونفت",
                "sentence": "Ich plane meine Zukunft.",
                "translation": "أنا أخطط لمستقبلي.",
                "explanation": "Zukunft means future.",
                "grammar": "Ich plane + object.",
                "question": "Was planst du?",
                "options": [
                    "Ich plane meine Zukunft.",
                    "Ich Zukunft gestern.",
                    "Planen ist blau."
                ],
                "answer": "Ich plane meine Zukunft.",
            },
        ],

        "advanced": [

            {
                "title": "Communication",
                "word": "Kommunikation",
                "meaning": "التواصل",
                "pronunciation": "كومونيكاتسيون",
                "sentence": "Gute Kommunikation ist wichtig.",
                "translation": "التواصل الجيد مهم.",
                "explanation": "Kommunikation means communication.",
                "grammar": "Noun + ist + adjective.",
                "question": "Was ist wichtig?",
                "options": [
                    "Gute Kommunikation.",
                    "Gestern ist blau.",
                    "Essen ist Kommunikation."
                ],
                "answer": "Gute Kommunikation.",
            },
        ],
    },


    # =====================================================
    # SWEDISH
    # =====================================================

    "swedish": {

        "beginner": [

            {
                "title": "Greeting",
                "word": "Hej",
                "meaning": "مرحبا",
                "pronunciation": "هاي",
                "sentence": "Hej, jag heter Ali.",
                "translation": "مرحباً، اسمي علي.",
                "explanation": "Hej means hello.",
                "grammar": "Jag heter + name.",
                "question": "Vad heter du?",
                "options": [
                    "Jag heter Ali.",
                    "Jag är igår.",
                    "Ali är blå."
                ],
                "answer": "Jag heter Ali.",
            },

            {
                "title": "Origin",
                "word": "Från",
                "meaning": "من",
                "pronunciation": "فرون",
                "sentence": "Jag kommer från Sverige.",
                "translation": "أنا من السويد.",
                "explanation": "Från means from.",
                "grammar": "Jag kommer från + place.",
                "question": "Var kommer du från?",
                "options": [
                    "Jag kommer från Sverige.",
                    "Jag äter Sverige.",
                    "Sverige är imorgon."
                ],
                "answer": "Jag kommer från Sverige.",
            },

            {
                "title": "Learning",
                "word": "Lära",
                "meaning": "يتعلم",
                "pronunciation": "ليرا",
                "sentence": "Jag lär mig engelska.",
                "translation": "أنا أتعلم الإنجليزية.",
                "explanation": "Lära sig means to learn.",
                "grammar": "Jag lär mig + language.",
                "question": "Vad lär du dig?",
                "options": [
                    "Jag lär mig engelska.",
                    "Engelska är igår.",
                    "Jag engelska blå."
                ],
                "answer": "Jag lär mig engelska.",
            },

            {
                "title": "Work",
                "word": "Arbeta",
                "meaning": "يعمل",
                "pronunciation": "أربيتا",
                "sentence": "Jag arbetar på en restaurang.",
                "translation": "أنا أعمل في مطعم.",
                "explanation": "Arbeta means to work.",
                "grammar": "Jag arbetar på + place.",
                "question": "Var arbetar du?",
                "options": [
                    "Jag arbetar på en restaurang.",
                    "Jag restaurang igår.",
                    "Arbeta är mat."
                ],
                "answer": "Jag arbetar på en restaurang.",
            },

            {
                "title": "Thank You",
                "word": "Tack",
                "meaning": "شكراً",
                "pronunciation": "تاك",
                "sentence": "Tack så mycket.",
                "translation": "شكراً جزيلاً.",
                "explanation": "Tack means thank you.",
                "grammar": "Tack så mycket is a common expression.",
                "question": "How do you say thank you?",
                "options": [
                    "Tack så mycket.",
                    "Hej igår.",
                    "Mat imorgon."
                ],
                "answer": "Tack så mycket.",
            },
        ],

        "intermediate": [

            {
                "title": "Daily Life",
                "word": "Vardag",
                "meaning": "الحياة اليومية",
                "pronunciation": "فارداغ",
                "sentence": "Min vardag är ganska lugn.",
                "translation": "حياتي اليومية هادئة إلى حد ما.",
                "explanation": "Vardag means everyday life.",
                "grammar": "Min + noun + är + adjective.",
                "question": "Hur är din vardag?",
                "options": [
                    "Min vardag är lugn.",
                    "Vardag är igår.",
                    "Jag vardag mat."
                ],
                "answer": "Min vardag är lugn.",
            },

            {
                "title": "Future",
                "word": "Framtid",
                "meaning": "المستقبل",
                "pronunciation": "فرام تيد",
                "sentence": "Jag planerar min framtid.",
                "translation": "أنا أخطط لمستقبلي.",
                "explanation": "Framtid means future.",
                "grammar": "Jag planerar + object.",
                "question": "Vad planerar du?",
                "options": [
                    "Jag planerar min framtid.",
                    "Jag framtid igår.",
                    "Framtid är mat."
                ],
                "answer": "Jag planerar min framtid.",
            },
        ],

        "advanced": [

            {
                "title": "Communication",
                "word": "Kommunikation",
                "meaning": "التواصل",
                "pronunciation": "كومونيكاتيون",
                "sentence": "Tydlig kommunikation är viktig.",
                "translation": "التواصل الواضح مهم.",
                "explanation": "Kommunikation means communication.",
                "grammar": "Adjective + noun + är + adjective.",
                "question": "Vad är viktigt?",
                "options": [
                    "Tydlig kommunikation.",
                    "Igår är blå.",
                    "Mat är kommunikation."
                ],
                "answer": "Tydlig kommunikation.",
            },
        ],
    },


    # =====================================================
    # THAI
    # =====================================================

    "thai": {

        "beginner": [

            {
                "title": "Hello",
                "word": "สวัสดี",
                "meaning": "مرحبا",
                "pronunciation": "سا-وات-دي",
                "sentence": "สวัสดีครับ",
                "translation": "مرحباً.",
                "explanation": "สวัสดี is a common Thai greeting.",
                "grammar": "ครับ is commonly used by male speakers.",
                "question": "How do you say hello?",
                "options": [
                    "สวัสดีครับ",
                    "ขอบคุณ",
                    "ลาก่อน"
                ],
                "answer": "สวัสดีครับ",
            },

            {
                "title": "Thank You",
                "word": "ขอบคุณ",
                "meaning": "شكراً",
                "pronunciation": "خوب خون",
                "sentence": "ขอบคุณครับ",
                "translation": "شكراً.",
                "explanation": "ขอบคุณ means thank you.",
                "grammar": "ครับ is commonly used by male speakers.",
                "question": "How do you say thank you?",
                "options": [
                    "ขอบคุณครับ",
                    "สวัสดีครับ",
                    "ไม่เป็นไร"
                ],
                "answer": "ขอบคุณครับ",
            },

            {
                "title": "Name",
                "word": "ชื่อ",
                "meaning": "اسم",
                "pronunciation": "تشُو",
                "sentence": "ผมชื่อ Ali.",
                "translation": "اسمي علي.",
                "explanation": "ชื่อ means name.",
                "grammar": "ผมชื่อ + name.",
                "question": "คุณชื่ออะไร?",
                "options": [
                    "ผมชื่อ Ali.",
                    "ผมกิน Ali.",
                    "Ali คือพรุ่งนี้."
                ],
                "answer": "ผมชื่อ Ali.",
            },

            {
                "title": "Food",
                "word": "อาหาร",
                "meaning": "طعام",
                "pronunciation": "آ-هان",
                "sentence": "ผมชอบอาหารไทย.",
                "translation": "أنا أحب الطعام التايلاندي.",
                "explanation": "อาหาร means food.",
                "grammar": "ชอบ means like.",
                "question": "คุณชอบอะไร?",
                "options": [
                    "ผมชอบอาหารไทย.",
                    "อาหารคือเมื่อวาน.",
                    "ผมชื่ออาหาร."
                ],
                "answer": "ผมชอบอาหารไทย.",
            },

            {
                "title": "Work",
                "word": "ทำงาน",
                "meaning": "يعمل",
                "pronunciation": "تام-غان",
                "sentence": "ผมทำงานที่ร้านอาหาร.",
                "translation": "أنا أعمل في مطعم.",
                "explanation": "ทำงาน means work.",
                "grammar": "ทำงานที่ + place.",
                "question": "คุณทำงานที่ไหน?",
                "options": [
                    "ผมทำงานที่ร้านอาหาร.",
                    "ผมร้านอาหารเมื่อวาน.",
                    "ทำงานคืออาหาร."
                ],
                "answer": "ผมทำงานที่ร้านอาหาร.",
            },
        ],

        "intermediate": [

            {
                "title": "Daily Life",
                "word": "ชีวิตประจำวัน",
                "meaning": "الحياة اليومية",
                "pronunciation": "تشيويت برا-جام وان",
                "sentence": "ชีวิตประจำวันของผมเรียบง่าย.",
                "translation": "حياتي اليومية بسيطة.",
                "explanation": "ชีวิตประจำวัน means daily life.",
                "grammar": "ของผม means my.",
                "question": "ชีวิตประจำวันของคุณเป็นอย่างไร?",
                "options": [
                    "ชีวิตประจำวันของผมเรียบง่าย.",
                    "ผมเป็นเมื่อวาน.",
                    "ชีวิตคืออาหาร."
                ],
                "answer": "ชีวิตประจำวันของผมเรียบง่าย.",
            },

            {
                "title": "Future",
                "word": "อนาคต",
                "meaning": "المستقبل",
                "pronunciation": "أ نا كوت",
                "sentence": "ผมวางแผนอนาคตของผม.",
                "translation": "أنا أخطط لمستقبلي.",
                "explanation": "อนาคต means future.",
                "grammar": "วางแผน means to plan.",
                "question": "คุณวางแผนอะไร?",
                "options": [
                    "ผมวางแผนอนาคตของผม.",
                    "อนาคตคือเมื่อวาน.",
                    "ผมอนาคตอาหาร."
                ],
                "answer": "ผมวางแผนอนาคตของผม.",
            },
        ],

        "advanced": [

            {
                "title": "Communication",
                "word": "การสื่อสาร",
                "meaning": "التواصل",
                "pronunciation": "كان سُو سان",
                "sentence": "การสื่อสารที่ดีเป็นสิ่งสำคัญ.",
                "translation": "التواصل الجيد شيء مهم.",
                "explanation": "การสื่อสาร means communication.",
                "grammar": "ที่ดี means good.",
                "question": "อะไรสำคัญ?",
                "options": [
                    "การสื่อสารที่ดี.",
                    "เมื่อวานเป็นสีฟ้า.",
                    "อาหารคือการสื่อสาร."
                ],
                "answer": "การสื่อสารที่ดี.",
            },
        ],
    },


    # =====================================================
    # CHINESE
    # =====================================================

    "chinese": {

        "beginner": [

            {
                "title": "Hello",
                "word": "你好",
                "meaning": "مرحبا",
                "pronunciation": "ني هاو",
                "sentence": "你好，我叫 Ali。",
                "translation": "مرحباً، اسمي علي.",
                "explanation": "你好 means hello.",
                "grammar": "我叫 + name means my name is.",
                "question": "你叫什么名字？",
                "options": [
                    "我叫 Ali。",
                    "我是昨天。",
                    "Ali 是蓝色。"
                ],
                "answer": "我叫 Ali。",
            },

            {
                "title": "Origin",
                "word": "来自",
                "meaning": "من / يأتي من",
                "pronunciation": "لاي تسي",
                "sentence": "我来自瑞典。",
                "translation": "أنا من السويد.",
                "explanation": "来自 means come from.",
                "grammar": "我来自 + place.",
                "question": "你来自哪里？",
                "options": [
                    "我来自瑞典。",
                    "我吃瑞典。",
                    "瑞典是明天。"
                ],
                "answer": "我来自瑞典。",
            },

            {
                "title": "Learning",
                "word": "学习",
                "meaning": "يتعلم",
                "pronunciation": "شيويه شي",
                "sentence": "我学习英语。",
                "translation": "أنا أتعلم الإنجليزية.",
                "explanation": "学习 means to study or learn.",
                "grammar": "我学习 + subject.",
                "question": "你学习什么？",
                "options": [
                    "我学习英语。",
                    "英语是昨天。",
                    "我英语蓝色。"
                ],
                "answer": "我学习英语。",
            },

            {
                "title": "Work",
                "word": "工作",
                "meaning": "عمل",
                "pronunciation": "غونغ زوو",
                "sentence": "我在餐厅工作。",
                "translation": "أنا أعمل في مطعم.",
                "explanation": "工作 means work.",
                "grammar": "在 + place + 工作.",
                "question": "你在哪里工作？",
                "options": [
                    "我在餐厅工作。",
                    "我餐厅昨天。",
                    "工作是食物。"
                ],
                "answer": "我在餐厅工作。",
            },

            {
                "title": "Thank You",
                "word": "谢谢",
                "meaning": "شكراً",
                "pronunciation": "شيه شيه",
                "sentence": "谢谢你。",
                "translation": "شكراً لك.",
                "explanation": "谢谢 means thank you.",
                "grammar": "谢谢你 = thank you.",
                "question": "How do you say thank you?",
                "options": [
                    "谢谢你。",
                    "你好。",
                    "再见。"
                ],
                "answer": "谢谢你。",
            },
        ],

        "intermediate": [

            {
                "title": "Daily Life",
                "word": "生活",
                "meaning": "الحياة",
                "pronunciation": "شِنگ هوو",
                "sentence": "我的生活很简单。",
                "translation": "حياتي بسيطة.",
                "explanation": "生活 means life or daily life.",
                "grammar": "我的 + noun.",
                "question": "你的生活怎么样？",
                "options": [
                    "我的生活很简单。",
                    "我的生活昨天。",
                    "生活是食物。"
                ],
                "answer": "我的生活很简单。",
            },

            {
                "title": "Future",
                "word": "未来",
                "meaning": "المستقبل",
                "pronunciation": "وي لاي",
                "sentence": "我计划我的未来。",
                "translation": "أنا أخطط لمستقبلي.",
                "explanation": "未来 means future.",
                "grammar": "计划 means to plan.",
                "question": "你计划什么？",
                "options": [
                    "我计划我的未来。",
                    "未来是昨天。",
                    "我未来食物。"
                ],
                "answer": "我计划我的未来。",
            },
        ],

        "advanced": [

            {
                "title": "Communication",
                "word": "沟通",
                "meaning": "التواصل",
                "pronunciation": "غو تونغ",
                "sentence": "良好的沟通非常重要。",
                "translation": "التواصل الجيد مهم جداً.",
                "explanation": "沟通 means communication.",
                "grammar": "非常 means very.",
                "question": "什么非常重要？",
                "options": [
                    "良好的沟通。",
                    "昨天是蓝色。",
                    "食物是沟通."
                ],
                "answer": "良好的沟通。",
            },
        ],
    },


    # =====================================================
    # SPANISH
    # =====================================================

    "spanish": {

        "beginner": [

            {
                "title": "Greeting",
                "word": "Hola",
                "meaning": "مرحبا",
                "pronunciation": "أولا",
                "sentence": "Hola, me llamo Ali.",
                "translation": "مرحباً، اسمي علي.",
                "explanation": "Hola means hello.",
                "grammar": "Me llamo + name.",
                "question": "¿Cómo te llamas?",
                "options": [
                    "Me llamo Ali.",
                    "Soy ayer.",
                    "Ali es azul."
                ],
                "answer": "Me llamo Ali.",
            },

            {
                "title": "Origin",
                "word": "De",
                "meaning": "من",
                "pronunciation": "دي",
                "sentence": "Soy de Suecia.",
                "translation": "أنا من السويد.",
                "explanation": "De means from/of depending on context.",
                "grammar": "Soy de + place.",
                "question": "¿De dónde eres?",
                "options": [
                    "Soy de Suecia.",
                    "Como Suecia.",
                    "Suecia es mañana."
                ],
                "answer": "Soy de Suecia.",
            },

            {
                "title": "Learning",
                "word": "Aprender",
                "meaning": "يتعلم",
                "pronunciation": "أبريندير",
                "sentence": "Estoy aprendiendo inglés.",
                "translation": "أنا أتعلم الإنجليزية.",
                "explanation": "Aprender means to learn.",
                "grammar": "Estoy + gerundio.",
                "question": "¿Qué estás aprendiendo?",
                "options": [
                    "Estoy aprendiendo inglés.",
                    "Inglés es ayer.",
                    "Estoy inglés azul."
                ],
                "answer": "Estoy aprendiendo inglés.",
            },

            {
                "title": "Work",
                "word": "Trabajar",
                "meaning": "يعمل",
                "pronunciation": "تراباخار",
                "sentence": "Trabajo en un restaurante.",
                "translation": "أنا أعمل في مطعم.",
                "explanation": "Trabajar means to work.",
                "grammar": "Trabajo en + place.",
                "question": "¿Dónde trabajas?",
                "options": [
                    "Trabajo en un restaurante.",
                    "Trabajo restaurante ayer.",
                    "Trabajar es comida."
                ],
                "answer": "Trabajo en un restaurante.",
            },

            {
                "title": "Thank You",
                "word": "Gracias",
                "meaning": "شكراً",
                "pronunciation": "غراسياس",
                "sentence": "Muchas gracias.",
                "translation": "شكراً جزيلاً.",
                "explanation": "Gracias means thank you.",
                "grammar": "Muchas gracias is a common expression.",
                "question": "How do you say thank you?",
                "options": [
                    "Muchas gracias.",
                    "Hola ayer.",
                    "Comida mañana."
                ],
                "answer": "Muchas gracias.",
            },
        ],

        "intermediate": [

            {
                "title": "Daily Life",
                "word": "Vida diaria",
                "meaning": "الحياة اليومية",
                "pronunciation": "ڤيدا دياريا",
                "sentence": "Mi vida diaria es tranquila.",
                "translation": "حياتي اليومية هادئة.",
                "explanation": "Vida diaria means daily life.",
                "grammar": "Mi + noun + es + adjective.",
                "question": "¿Cómo es tu vida diaria?",
                "options": [
                    "Mi vida diaria es tranquila.",
                    "Mi vida ayer.",
                    "Vida es comida."
                ],
                "answer": "Mi vida diaria es tranquila.",
            },

            {
                "title": "Future",
                "word": "Futuro",
                "meaning": "المستقبل",
                "pronunciation": "فوتورو",
                "sentence": "Estoy planeando mi futuro.",
                "translation": "أنا أخطط لمستقبلي.",
                "explanation": "Futuro means future.",
                "grammar": "Estoy planeando + object.",
                "question": "¿Qué estás planeando?",
                "options": [
                    "Estoy planeando mi futuro.",
                    "Mi futuro ayer.",
                    "Futuro es comida."
                ],
                "answer": "Estoy planeando mi futuro.",
            },
        ],

        "advanced": [

            {
                "title": "Communication",
                "word": "Comunicación",
                "meaning": "التواصل",
                "pronunciation": "كومونيكاسيون",
                "sentence": "La comunicación clara es muy importante.",
                "translation": "التواصل الواضح مهم جداً.",
                "explanation": "Comunicación means communication.",
                "grammar": "La + noun + es + adjective.",
                "question": "¿Qué es importante?",
                "options": [
                    "La comunicación clara.",
                    "Ayer es azul.",
                    "La comida es comunicación."
                ],
                "answer": "La comunicación clara.",
            },
        ],
    },
}


# =========================================================
# USER PROGRESS
# =========================================================

def get_progress(context, language):

    if "language_progress" not in context.user_data:
        context.user_data["language_progress"] = {}

    if language not in context.user_data["language_progress"]:
        context.user_data["language_progress"][language] = {
            "points": 0,
            "correct": 0,
            "wrong": 0,
            "completed": [],
            "streak": 0,
            "last_level": "beginner",
        }

    return context.user_data["language_progress"][language]


def add_points(context, language, amount):

    progress = get_progress(
        context,
        language,
    )

    progress["points"] += amount


# =========================================================
# VOICE / TTS
# =========================================================

async def send_voice(
    update: Update,
    language: str,
    text: str,
):

    if not update.effective_chat:
        return

    language_info = LANGUAGES.get(language)

    if not language_info:
        return

    try:

        audio = io.BytesIO()

        tts = gTTS(
            text=text,
            lang=language_info["tts"],
            slow=False,
        )

        tts.write_to_fp(audio)

        audio.seek(0)

        await update.effective_chat.send_audio(
            audio=audio,
            title=f"{language_info['native']} pronunciation",
            performer="UNKNOWN WORLD AI",
        )

    except Exception as error:

        logger.exception(
            "TTS error: %s",
            error,
        )

        if update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ تعذر إنشاء الصوت حالياً.\n"
                "النطق المكتوب ما زال متاحاً."
            )


# =========================================================
# MAIN LANGUAGE MENU
# =========================================================

def language_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🇬🇧 English",
                callback_data="lang_english"
            ),
            InlineKeyboardButton(
                "🇩🇪 German",
                callback_data="lang_german"
            ),
        ],

        [
            InlineKeyboardButton(
                "🇸🇪 Swedish",
                callback_data="lang_swedish"
            ),
            InlineKeyboardButton(
                "🇹🇭 Thai",
                callback_data="lang_thai"
            ),
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 Chinese",
                callback_data="lang_chinese"
            ),
            InlineKeyboardButton(
                "🇪🇸 Spanish",
                callback_data="lang_spanish"
            ),
        ],

        [
            InlineKeyboardButton(
                "🔙 Back",
                callback_data="main_menu"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# LEVEL MENU
# =========================================================

def level_menu(language):

    keyboard = [

        [
            InlineKeyboardButton(
                "🟢 Beginner",
                callback_data=f"lang_{language}_level_beginner"
            )
        ],

        [
            InlineKeyboardButton(
                "🟡 Intermediate",
                callback_data=f"lang_{language}_level_intermediate"
            )
        ],

        [
            InlineKeyboardButton(
                "🔴 Advanced",
                callback_data=f"lang_{language}_level_advanced"
            )
        ],

        [
            InlineKeyboardButton(
                "📊 My Progress",
                callback_data=f"lang_{language}_progress"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 Languages",
                callback_data="languages"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# LESSON KEYBOARD
# =========================================================

def lesson_keyboard(
    language,
    level,
    number,
    total,
):

    buttons = [

        [
            InlineKeyboardButton(
                "🧠 Quiz",
                callback_data=(
                    f"lang_{language}_quiz_{level}_{number}"
                ),
            ),

            InlineKeyboardButton(
                "🔊 Pronunciation",
                callback_data=(
                    f"lang_{language}_pronounce_{level}_{number}"
                ),
            ),
        ],
    ]

    if number < total:

        buttons.append(
            [
                InlineKeyboardButton(
                    "➡️ Next Lesson",
                    callback_data=(
                        f"lang_{language}_next_{level}_{number}"
                    ),
                )
            ]
        )

    buttons.append(
        [
            InlineKeyboardButton(
                "📊 Progress",
                callback_data=f"lang_{language}_progress"
            )
        ]
    )

    buttons.append(
        [
            InlineKeyboardButton(
                "🔙 Levels",
                callback_data=f"lang_{language}"
            )
        ]
    )

    return InlineKeyboardMarkup(buttons)


# =========================================================
# LESSON DISPLAY
# =========================================================

async def show_lesson(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
    level,
    number,
):

    lessons = LESSONS[language][level]

    if number < 1:
        number = 1

    if number > len(lessons):
        number = len(lessons)

    lesson = lessons[number - 1]

    progress = get_progress(
        context,
        language,
    )

    progress["last_level"] = level

    text = (
        f"{LANGUAGES[language]['name']}\n"
        f"📚 {LEVELS[level]}\n\n"
        f"Lesson {number}/{len(lessons)}\n"
        f"━━━━━━━━━━━━━━\n\n"
        f"📌 {lesson['title']}\n\n"
        f"📝 Word:\n"
        f"{lesson['word']}\n\n"
        f"🇦🇪 Meaning:\n"
        f"{lesson['meaning']}\n\n"
        f"🔊 Pronunciation:\n"
        f"{lesson['pronunciation']}\n\n"
        f"💬 Sentence:\n"
        f"{lesson['sentence']}\n\n"
        f"🇦🇪 Translation:\n"
        f"{lesson['translation']}\n\n"
        f"💡 Explanation:\n"
        f"{lesson['explanation']}\n\n"
        f"📖 Grammar:\n"
        f"{lesson['grammar']}"
    )

    if update.callback_query:

        await update.callback_query.edit_message_text(
            text,
            reply_markup=lesson_keyboard(
                language,
                level,
                number,
                len(lessons),
            ),
        )

    elif update.effective_message:

        await update.effective_message.reply_text(
            text,
            reply_markup=lesson_keyboard(
                language,
                level,
                number,
                len(lessons),
            ),
        )


# =========================================================
# LANGUAGE HOME
# =========================================================

async def languages(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = (
        "🎓 LANGUAGE LEARNING\n\n"
        "Learn languages step by step with:\n\n"
        "📚 Lessons\n"
        "📝 Vocabulary\n"
        "💬 Sentences\n"
        "📖 Grammar\n"
        "🔊 Voice Pronunciation\n"
        "🧠 Quizzes\n"
        "🏆 Points\n"
        "📊 Progress\n"
        "🔄 Review\n\n"
        "Choose a language:"
    )

    if update.callback_query:

        await update.callback_query.edit_message_text(
            text,
            reply_markup=language_menu(),
        )

    elif update.effective_message:

        await update.effective_message.reply_text(
            text,
            reply_markup=language_menu(),
        )


# =========================================================
# LEVEL DISPLAY
# =========================================================

async def show_level(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
    level,
):

    lessons = LESSONS[language][level]

    text = (
        f"{LANGUAGES[language]['name']}\n\n"
        f"{LEVELS[level]}\n\n"
        f"📚 Available lessons: {len(lessons)}\n\n"
        "Choose a lesson:"
    )

    keyboard = []

    for index, lesson in enumerate(
        lessons,
        start=1,
    ):

        keyboard.append(
            [
                InlineKeyboardButton(
                    f"📘 {index}. {lesson['title']}",
                    callback_data=(
                        f"lang_{language}_lesson_"
                        f"{level}_{index}"
                    ),
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                "🔙 Levels",
                callback_data=f"lang_{language}"
            )
        ]
    )

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# =========================================================
# QUIZ
# =========================================================

async def show_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
    level,
    number,
):

    lessons = LESSONS[language][level]

    if number < 1 or number > len(lessons):
        number = 1

    lesson = lessons[number - 1]

    keyboard = []

    for index, option in enumerate(
        lesson["options"]
    ):

        letter = chr(
            97 + index
        )

        keyboard.append(
            [
                InlineKeyboardButton(
                    f"{letter.upper()}. {option}",
                    callback_data=(
                        f"lang_{language}_answer_"
                        f"{letter}_{level}_{number}"
                    ),
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                "🔙 Back to Lesson",
                callback_data=(
                    f"lang_{language}_lesson_"
                    f"{level}_{number}"
                ),
            )
        ]
    )

    text = (
        f"🧠 QUIZ\n\n"
        f"{LANGUAGES[language]['name']}\n"
        f"{LEVELS[level]}\n\n"
        f"❓ {lesson['question']}\n\n"
        "Choose the correct answer:"
    )

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# =========================================================
# QUIZ ANSWER
# =========================================================

async def answer_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
    level,
    number,
    answer,
):

    lessons = LESSONS[language][level]

    if number < 1 or number > len(lessons):
        number = 1

    lesson = lessons[number - 1]

    progress = get_progress(
        context,
        language,
    )

    option_index = ord(answer) - 97

    if (
        option_index < 0
        or option_index >= len(lesson["options"])
    ):
        return

    selected = lesson["options"][option_index]

    if selected == lesson["answer"]:

        progress["correct"] += 1
        progress["streak"] += 1

        add_points(
            context,
            language,
            10,
        )

        if number not in progress["completed"]:

            progress["completed"].append(
                number
            )

        text = (
            "✅ CORRECT!\n\n"
            "🎉 Excellent!\n\n"
            f"Answer:\n"
            f"{lesson['answer']}\n\n"
            "🏆 +10 points\n"
            f"🔥 Streak: {progress['streak']}"
        )

    else:

        progress["wrong"] += 1
        progress["streak"] = 0

        text = (
            "❌ NOT QUITE\n\n"
            f"Your answer:\n"
            f"{selected}\n\n"
            f"✅ Correct answer:\n"
            f"{lesson['answer']}\n\n"
            "📚 Review the lesson and try again."
        )

    keyboard = [

        [
            InlineKeyboardButton(
                "📘 Review Lesson",
                callback_data=(
                    f"lang_{language}_lesson_"
                    f"{level}_{number}"
                ),
            )
        ],

        [
            InlineKeyboardButton(
                "🧠 Try Quiz Again",
                callback_data=(
                    f"lang_{language}_quiz_"
                    f"{level}_{number}"
                ),
            )
        ],

        [
            InlineKeyboardButton(
                "➡️ Next Lesson",
                callback_data=(
                    f"lang_{language}_next_"
                    f"{level}_{number}"
                ),
            )
        ],

        [
            InlineKeyboardButton(
                "📊 Progress",
                callback_data=(
                    f"lang_{language}_progress"
                ),
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# =========================================================
# PRONUNCIATION + REAL AUDIO
# =========================================================

async def show_pronunciation(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
    level,
    number,
):

    lessons = LESSONS[language][level]

    if number < 1 or number > len(lessons):
        number = 1

    lesson = lessons[number - 1]

    text = (
        "🔊 PRONUNCIATION\n\n"
        f"{LANGUAGES[language]['name']}\n\n"
        f"📝 Word:\n"
        f"{lesson['word']}\n\n"
        f"🔊 Arabic pronunciation:\n"
        f"{lesson['pronunciation']}\n\n"
        f"💬 Example:\n"
        f"{lesson['sentence']}\n\n"
        "🎧 Sending pronunciation audio..."
    )

    keyboard = [

        [
            InlineKeyboardButton(
                "📘 Back to Lesson",
                callback_data=(
                    f"lang_{language}_lesson_"
                    f"{level}_{number}"
                ),
            )
        ]
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

    # Send the word pronunciation.
    await send_voice(
        update,
        language,
        lesson["word"],
    )

    # Send the complete sentence pronunciation.
    await send_voice(
        update,
        language,
        lesson["sentence"],
    )


# =========================================================
# PROGRESS
# =========================================================

async def show_progress(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
):

    progress = get_progress(
        context,
        language,
    )

    total_completed = len(
        progress["completed"]
    )

    points = progress["points"]
    correct = progress["correct"]
    wrong = progress["wrong"]
    streak = progress["streak"]

    total_answers = correct + wrong

    if total_answers > 0:

        accuracy = round(
            correct / total_answers * 100
        )

    else:

        accuracy = 0

    text = (
        "📊 YOUR LANGUAGE PROGRESS\n\n"
        f"{LANGUAGES[language]['name']}\n"
        "━━━━━━━━━━━━━━\n\n"
        f"🏆 Points: {points}\n"
        f"📚 Lessons completed: {total_completed}\n"
        f"✅ Correct answers: {correct}\n"
        f"❌ Wrong answers: {wrong}\n"
        f"🎯 Accuracy: {accuracy}%\n"
        f"🔥 Current streak: {streak}\n\n"
        "Keep practicing every day!"
    )

    keyboard = [

        [
            InlineKeyboardButton(
                "📚 Continue Learning",
                callback_data=f"lang_{language}"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 Languages",
                callback_data="languages"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# =========================================================
# NEXT LESSON
# =========================================================

async def next_lesson(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    language,
    level,
    number,
):

    next_number = number + 1

    lessons = LESSONS[language][level]

    if next_number > len(lessons):

        text = (
            "🎉 LEVEL COMPLETED!\n\n"
            f"{LANGUAGES[language]['name']}\n"
            f"{LEVELS[level]}\n\n"
            "You completed all lessons in this level.\n\n"
            "🏆 Great work!"
        )

        keyboard = [

            [
                InlineKeyboardButton(
                    "📊 My Progress",
                    callback_data=(
                        f"lang_{language}_progress"
                    ),
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 Levels",
                    callback_data=f"lang_{language}"
                )
            ],
        ]

        await update.callback_query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

        return

    await show_lesson(
        update,
        context,
        language,
        level,
        next_number,
    )


# =========================================================
# TEXT PRACTICE
# =========================================================

async def language_text_practice(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if not update.effective_message:
        return

    text = update.effective_message.text

    if not text:
        return

    # Normal text messages continue to the main chat handler.
    return


# =========================================================
# CALLBACK ROUTER
# =========================================================

async def language_lesson(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    if not query:
        return

    data = query.data

    try:
        await query.answer()
    except Exception:
        pass

    # -----------------------------------------------------
    # LANGUAGE HOME
    # -----------------------------------------------------

    if data == "languages":

        await languages(
            update,
            context,
        )

        return

    # -----------------------------------------------------
    # LANGUAGE CALLBACKS
    # -----------------------------------------------------

    if data.startswith("lang_"):

        value = data[5:]

        parts = value.split("_")

        if not parts:
            return

        language = parts[0]

        if language not in LANGUAGES:
            return

        # -------------------------------------------------
        # LANGUAGE HOME
        # lang_english
        # -------------------------------------------------

        if len(parts) == 1:

            await query.edit_message_text(
                f"{LANGUAGES[language]['name']}\n\n"
                "Choose your level:",
                reply_markup=level_menu(language),
            )

            return

        action = parts[1]

        # -------------------------------------------------
        # LEVEL
        # -------------------------------------------------

        if action == "level":

            if len(parts) < 3:
                return

            level = parts[2]

            if level not in LEVELS:
                return

            await show_level(
                update,
                context,
                language,
                level,
            )

            return

        # -------------------------------------------------
        # LESSON
        # -------------------------------------------------

        if action == "lesson":

            if len(parts) < 4:
                return

            level = parts[2]

            try:

                number = int(
                    parts[3]
                )

            except ValueError:

                return

            if level not in LESSONS[language]:
                return

            await show_lesson(
                update,
                context,
                language,
                level,
                number,
            )

            return

        # -------------------------------------------------
        # QUIZ
        # -------------------------------------------------

        if action == "quiz":

            if len(parts) < 4:
                return

            level = parts[2]

            try:

                number = int(
                    parts[3]
                )

            except ValueError:

                return

            if level not in LESSONS[language]:
                return

            await show_quiz(
                update,
                context,
                language,
                level,
                number,
            )

            return

        # -------------------------------------------------
        # ANSWER
        # -------------------------------------------------

        if action == "answer":

            if len(parts) < 5:
                return

            answer = parts[2]

            level = parts[3]

            try:

                number = int(
                    parts[4]
                )

            except ValueError:

                return

            if level not in LESSONS[language]:
                return

            await answer_quiz(
                update,
                context,
                language,
                level,
                number,
                answer,
            )

            return

        # -------------------------------------------------
        # PRONUNCIATION
        # -------------------------------------------------

        if action == "pronounce":

            if len(parts) < 4:
                return

            level = parts[2]

            try:

                number = int(
                    parts[3]
                )

            except ValueError:

                return

            if level not in LESSONS[language]:
                return

            await show_pronunciation(
                update,
                context,
                language,
                level,
                number,
            )

            return

        # -------------------------------------------------
        # PROGRESS
        # -------------------------------------------------

        if action == "progress":

            await show_progress(
                update,
                context,
                language,
            )

            return

        # -------------------------------------------------
        # NEXT
        # -------------------------------------------------

        if action == "next":

            if len(parts) < 4:
                return

            level = parts[2]

            try:

                number = int(
                    parts[3]
                )

            except ValueError:

                return

            if level not in LESSONS[language]:
                return

            await next_lesson(
                update,
                context,
                language,
                level,
                number,
            )

            return


# =========================================================
# OPTIONAL AUDIO HELPER
# =========================================================

async def send_pronunciation_audio(
    update: Update,
    language: str,
    text: str,
):

    await send_voice(
        update,
        language,
        text,
    )


# =========================================================
# EXPORT
# =========================================================

__all__ = [
    "languages",
    "language_lesson",
    "language_text_practice",
    "send_pronunciation_audio",
    "send_voice",
    "LANGUAGES",
    "LEVELS",
    "LESSONS",
]
