from telegram import ReplyKeyboardRemove, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

# Function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    if 'language' in context.user_data:
        await send_main_menu(update, context)
    else:
        language_keyboard = [['Қазақша', 'Русский', 'English']]
        await update.message.reply_text(
            '''
🎓 Қош келдіңіз! Мен Караганды индустриалды университетінің ботымын. Бот арқылы университетке түсу туралы ақпарат алуға болады. 😊

📘 Вас приветствует бот Карагандинского индустриального университета! Я помогу вам получить информацию о поступлении. 😊

🏛️ Bot of the Karagandy Industrial University welcomes you! I will help you get information about enrollment. 😊

Тілді таңдаңыз / Выберите язык / Choose language:''',
            reply_markup=ReplyKeyboardMarkup(language_keyboard, resize_keyboard=True)
        )

# Function to handle language selection
async def choose_language(update: Update, context: CallbackContext) -> None:
    language = update.message.text
    context.user_data['language'] = language
    await send_main_menu(update, context)

# Function to change language
async def change_language(update: Update, context: CallbackContext) -> None:
    language_keyboard = [['Қазақша', 'Русский', 'English']]
    await update.message.reply_text(
        'Тілді таңдаңыз / Выберите язык / Choose language:',
        reply_markup=ReplyKeyboardMarkup(language_keyboard, resize_keyboard=True)
    )

# Function to send the main menu
async def send_main_menu(update: Update, context: CallbackContext) -> None:
    language = context.user_data.get('language')

    if language == 'Қазақша':
        main_menu = [['📌 Университетке қабылдау туралы ақпарат'], ['📞 Байланыс'], ['📄 Қабылдау комиссиясына қажетті құжаттар тізімі'], ['🖊️ Грант байқауы туралы ақпарат'], ['📅 Маңызды күндер'], ['📘 Оқу бағдарламалары'], ['🌟 Біздің университеттің артықшылықтары'], ['❓ Басқа сұрақ'], ['🌐 Тілді ауыстыру/Change language/Поменять язык']]
        welcome_text = '''
        Мәзірге қош келдіңіз!
        
    📌 Университетке қабылдау туралы ақпарат - қабылдауға қажетті негізгі ақпарат

    📞 Байланыс - университеттің қабылдау комиссиясының байланыс деректерін таба аласыз
    
    📄 Қабылдау комиссиясына қажетті құжаттар тізімі - университеттке қабылдауға қандай құжаттар қажет екенін білуге болады

    🖊️ Грант байқауы туралы ақпарат - грант байқауы туралы ақпаратты біле аласыз
    
    📅 Маңызды күндер - маңызды күндер мен оқиғаларды бақылай аласыз
    
    📘 Оқу бағдарламалары - университет ұсынатын оқу бағдарламаларымен және оқу бағдарламасына басып, кім болып жұмыс істей алатыныңызды, бағдарлама туралы қосымша ақпаратпен таныса аласыз
    
    🌟 Біздің университеттің артықшылықтары - неліктен біздің университетті таңдау керек екенін біле аласыз
    
    ❓ Басқа сұрақ - мәзердегі ақпарттан басқа қосымша сұрақтарыңыз болса, қоя аласыз
    
    🌐 Тілді ауыстыру/Change language/Поменять язык - ботпен тілдесу тілін өзгертіңіз'''
    elif language == 'Русский':
        main_menu = [['📌 Информация о поступлении'], ['📞 Контакты'], ['📄 Список документов для приемной комиссии'], ['🖊️ Информация о конкурсе грантов'], ['📅 Важные даты'], ['📘 Образовательные программы'], ['🌟 Преимущества нашего университета'], ['❓ Другой вопрос'], ['🌐 Тілді ауыстыру/Change language/Поменять язык']]
        welcome_text = '''
        Добро пожаловать в меню!
        
    📌 Информация о поступлении - получите основную информацию, необходимую для поступления
    
    📞 Контакты - найдите контактные данные приёмной комиссии университета
    
    📄 Список документов - узнайте, какие документы нужны для поступления

    🖊️ Информация о конкурсе грантов - получите информацию об образовательных грантах
    
    📅 Важные даты - узнайте важные даты и события
    
    📘 Образовательные программы - ознакомьтесь с программами обучения, предлагаемыми университетом и узнайте, кем вы сможете работать, нажав на образовательную программу

    🌟 Преимущества нашего университета - узнайте, почему стоит выбрать наш университет

    ❓ Другой вопрос- можете задайть любые другие вопросы, которые у вас могут возникнуть
    
    🌐 Тілді ауыстыру/Change language/Поменять язык - измените язык общения с ботом.
        '''
    elif language == 'English':
        main_menu = [['📌 Addmission information'], ['📞 Contacts'], ['📄 List of Documents'], ['🖊️ Information about grants'], ['📅 Important dates'], ['📘 Educational Programs'], ['🌟 Advantages of our university'], ['❓ Other Question'], ['🌐 Тілді ауыстыру/Change language/Поменять язык']]
        welcome_text = '''
        Welcome to the menu!
        
    📌 Addmission information - get the main information needed for enrollment
    
    📞 Contacts - find the contact details of the university's addmission committee

    📄 List of Documents - find out which documents are needed for enrollment

    📅 Important Dates - find information about important dates and events

    📘 Educational Programs - explore the educational programs offered by the university, and find out, where you can work by clicking on educational program

    🌟 Advantages of our University - find out why you should choose our university

    ❓ Other Question - ask any other questions you may have
    
    🌐 Тілді ауыстыру/Change language/Поменять язык - change the language of interaction with the bot.
        '''
    else:
        await update.message.reply_text('''
Кешіріңіз, пайдаланушының тілін анықтау мүмкін болмады. Өз қалаған тіліңізді таңдап жазыңыз: Қазақша|Орысша|English.
                                        
Извините, не удалось определить язык пользователя. Выберите и напишите один из языков: Қазақша|Русский|English.

Sorry, the user's language could not be determined. Choose and write one of the languages: Қазақша|Русский|English.''')
        return

    await update.message.reply_text(
        welcome_text,
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

# Функция обработки основного меню
async def main_menu(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text in ['📌 Информация о поступлении', '📌 Addmission information', '📌 Университетке қабылдау туралы ақпарат']:
        if text == "📌 Университетке қабылдау туралы ақпарат":
            info = '''Барлық талапкерлер үшін Университетке қабылдау туралы ақпарат:

1\. 🎓 Колледж түлектері ҰБТ тапсырусыз ақылы оқуға түсе алады \(сұхбат негізінде\)\.

2\. 📚 Жоғары білім базасында оқуға түсетін талапкерлер мен шетел азаматтары үшін түсу емтихандары сұхбат нысанында өткізіледі\.

3\. 🏠 Барлық қаладан тыс тұратын студенттер үшін жатақхана беріледі\.

4\. 🎓 Грантқа ҰТО арқылы жеке кабинетте беру керек, бірақ *ДЕРЕКТЕР ЖАҚЫН МАҢДАҒЫ УНИВЕРСИТЕТТТТЕ РАССТАЛУЫ КЕРЕК*\.

🏛️ Қарағанды индустриалды университетінің қабылдау комиссиясы сізді өтініште көрсетілген жеке деректерді растауға шақырады\. Өзіңізбен бірге құжаттардың түпнұсқалары болуы керек\.'''
            await update.message.reply_markdown_v2(info)
        elif text == "📌 Addmission information":
            info = '''Addmission information for all future students:

1\. 🎓 College graduates enroll in paid education without passing the UNT \(based on an interview\)\.

2\. 📚 Entrance exams for applicants entering higher education and foreign citizens are conducted in the form of an interview\.

3\. 🏠 A dormitory is provided for all nonresident students\.

4\. 🎓 You need to apply for a grant through the NTC in your personal account, but *THE DATA MUST BE CONFIRMED* at the university of the nearest city\.

🏛️ The Admission Committee of Karaganda Industrial University invites you to confirm the personal data specified in the application\. Have the original documents with you\.'''
            await update.message.reply_markdown_v2(info)
        elif text == "📌 Информация о поступлении":
            info = '''Информация о поступлении для всех абитуриентов:
1\. 🎓 Выпускники колледжей на платное обучение поступают без сдачи ЕНТ \(на основе собеседования\)\.

2\. 📚 Вступительные экзамены для абитуриентов, поступающих на базе высшего образования и иностранных граждан, проводятся в форме собеседования\.

3\. 🏠 Для всех иногородних студентов предоставляется общежитие\.

4\. 🎓 На грант нужно подать через НЦТ в личном кабинете, но *ДАННЫЕ ДОЛЖНЫ БЫТЬ ПОДТВЕРЖДЕНЫ* в университете ближайшего города\.

🏛️ Приемная комиссия Карагандинского индустриального университета приглашает Вас подтвердить личные данные, указанные в заявлении\. При себе иметь оригиналы документов\.'''
            await update.message.reply_markdown_v2(info)
    
    elif text in ['Қазақша', 'Русский', 'English']:
        language = update.message.text
        context.user_data['language'] = language

        await send_main_menu(update, context)
    
    elif text in ['📞 Контакты', '📞 Contacts', '📞 Байланыс']:
        if text == "📞 Контакты":
            contacts = '''Контакты приемной комиссии:
    📞 Телефон:
    - 8(7213) 91 65 61
    - 8(701) 430 64 14
    - 8(700) 569 06 47
    - 8(777) 735 95 07

    📧 Почта: front_office@tttu.edu.kz  
    🌐 Сайт: www.tttu.edu.kz

    🕒 График работы:
    - Понедельник-пятница: 9:00-18:00 
                     Обед: 13:00-14:00
    - Суббота: 9:00-13:00
    🏢 Адрес:
    101400, Казахстан, Карагандинская область, г. Темиртау, пр. Республики, 30, Новое здание'''
            await update.message.reply_text(contacts)
        elif text == "📞 Contacts":
            contacts = '''Contacts of the Admissions Committee:

    📞 Phone:
    - 8 (7213) 91 65 61
    - 8 (701) 430 64 14
    - 8 (700) 569 06 47
    - 8 (777) 735 95 07

    📧 Mail: front_office@tttu.edu.kz  
    🌐 Website: www.tttu.edu.kz

    🕒 Opening Hours:
    - Monday-Friday: 9:00 - 18:00  
              Lunch: 13:00 - 14:00
    - Saturday: 9:00 - 13:00

    🏢 Address:  
    30, Republic Ave., Temirtau, Karaganda region, 101400, Kazakhstan, New building'''
            await update.message.reply_text(contacts)
        elif text == "📞 Байланыс":
            contacts = '''Қабылдау комиссиясының байланыстары:

    📞 Телефон:
    - 8 (7213) 91 65 61
    - 8 (701) 430 64 14
    - 8 (700) 569 06 47
    - 8 (777) 735 95 07

    📧 Пошта: front_office@tttu.edu.kz  
    🌐 Сайт: www.tttu.edu.kz

    🕒 Жұмыс кестесі:
    - Дүйсенбі-жұма: 9:00 - 18:00  
           Түскі ас: 13:00 - 14:00
    - Сенбі: 9:00 - 13:00

    🏢 Мекен-жайы:  
    101400, Қазақстан, Қарағанды облысы, Теміртау қаласы, Республика даңғылы, 30, жаңа ғимарат'''
            await update.message.reply_text(contacts)
    
    elif text in ['📅 Important dates', "📅 Важные даты", "📅 Маңызды күндер"]:
        if text == '📅 Important dates':
            dates = '''
*Important Dates for Bachelors:*

📅 *20 June – 25 August*  
Acceptance of documents

📅 *13 – 20 July*  
Submission for an educational grant

📅 *1 August*  
Results of the educational grant competition

\-\-\-

*Important Dates for Masters:*

📅 *June 1 – July 15* 
Acceptance of applications for participation in CT on the NTC website

📅 *July 20 – August 10* 
CT will be held in computer format at U\-Study

📅 *August 12 – 20*  
Competition

📅 *August 28*  
Admission to the Master's program

\-\-\-

*Important Dates for Doctors:*

📅 *July 3 – August 3*  
Acceptance of applications

📅 *August 4 – 20*  
Entrance exams  
\- The certificate of the entrance exam held from August 4 to August 20 is valid until December 1 of the current calendar year\.

📅 *August 15 – 28*  
Enrollment  
\- When submitting documents, the applicant indicates one OVPO and one group of educational programs\.
'''
            await update.message.reply_markdown_v2(dates)
        elif text == "📅 Важные даты":
            dates = '''
*Важные даты для бакалавров:*

📅 *20 июня – 25 августа*  
Прием документов

📅 *13 – 20 июля*  
Подача на образовательный грант

📅 *1 августа*  
Результаты конкурса образовательных грантов

\-\-\-

*Важные даты для магистрантов:*

📅 *1 июня – 15 июля*  
Прием заявлений на участие в КТ на сайте НЦТ

📅 *20 июля – 10 августа*  
КТ пройдет в компьютерном формате в U\-Study

📅 *12 – 20 августа*  
Конкурс

📅 *28 августа*  
Зачисление в магистратуру

\-\-\-

*Важные даты для докторантов:*

📅 *3 июля – 3 августа*  
Прием заявлений

📅 *4 – 20 августа*  
Вступительные экзамены  
\- Сертификат вступительного экзамена, проведенного в период с 4 по 20 августа, действителен до 1 декабря текущего календарного года\.

📅 *15 – 28 августа*  
Зачисление  
\- При подаче документов поступающий указывает одну ОВПО и одну группу образовательных программ\.'''
            await update.message.reply_markdown_v2(dates)
        elif text == "📅 Маңызды күндер":
            dates = '''
*Бакалаврлар үшін маңызды күндер:*

📅 *20 маусым \- 25 тамыз*  
Құжаттарды қабылдау

📅 *13 \- 20 шілде*  
Білім беру грантына өтініш беру

📅 *1 тамыз*  
Білім беру грантының конкурсының нәтижелері

\-\-\-

*Магистранттар үшін маңызды күндер:*

📅 *1 маусым \- 15 шілде*  
ҰТО сайтында КТ\-ға қатысуға өтініштер қабылдау

📅 *20 шілде \- 10 тамыз*  
КТ компьютерлік форматта U\-Study\-де өтеді

📅 *12 \- 20 тамыз*  
Байқау

📅 *28 тамыз*  
Магистратураға қабылдау

\-\-\-

*Докторанттар үшін маңызды күндер:*

📅 *3 шілде \- 3 тамыз*  
Өтініштерді қабылдау

📅 *4 \- 20 тамыз*  
Қабылдау емтихандары  
   \- 4 \- 20 тамыз аралығында өткізілген қабылдау емтиханының сертификаты ағымдағы күнтізбелік жылдың 1 желтоқсанына дейін жарамды\.

📅 *15 \- 28 тамыз*  
Оқуға қабылдау  
   \- Құжаттарды тапсыру кезінде оқуға түсуші бір ЖЖОКБҰ мен білім беру бағдарламаларының бір тобын көрсетеді\.'''
            await update.message.reply_markdown_v2(dates)

    elif text in ['📄 Список документов для приемной комиссии', '📄 List of Documents', '📄 Қабылдау комиссиясына қажетті құжаттар тізімі']:
        if text == '📄 Список документов для приемной комиссии':
            programs_keyboard = [['Список документов для бакалавриата'], ['Список документов для магистратуры'], ['Список документов для докторантуры'], ['↩️ Назад в меню']]
            await update.message.reply_text(
                'Выберите уровень образовательной программы:',
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
        elif text == '📄 Қабылдау комиссиясына қажетті құжаттар тізімі':
            programs_keyboard = [['Бакалавриат деңгейіне құжаттар тізімі'], ['Магистратура деңгейіне құжаттар тізімі'], ['Докторантура деңгейіне құжаттар тізімі'], ['↩️ Мәзірге оралу']]
            await update.message.reply_text(
                'Білім беру бағдарламасының деңгейін таңдаңыз:',
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
        elif text == '📄 List of Documents':
            programs_keyboard = [["List of Documents for Bachelor's degree"], ["List of Documents for Masters's degree"], ["List of Documents for Doctor's degree"], ['↩️ Back to the menu']]
            await update.message.reply_text(
                'Select the level of the educational program:',
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
    elif text == "Бакалавриат деңгейіне құжаттар тізімі":
        documents = '''Қабылдау комиссиясына арналған құжаттар тізімі:
1. Қабылдау туралы өтініш (қабылдау комиссиясында толтырылады).
2. Қосымшасы бар білім туралы құжат (түпнұсқа).
3. Білім беру грантын беру туралы куәлік (бар болса).
4. ҰБТ немесе КТ сертификаты.
5. 3х4 өлшемді 6 фотокарта.
6. Флюорография суреті бар 075/Е нысанындағы медициналық анықтама.
7. Егу картасының көшірмесі (063-нысан).
8. Жеке басын куәландыратын құжаттың көшірмесі-3 дана.
9. Тіркеу куәлігінің немесе әскери билеттің көшірмесі (жігіттер үшін).
10. Еңбек кітапшасының көшірмесі (бар болса).
11. Жеке істі қалыптастыру үшін: құжат тігілетін мұқаба, картон конверт(Еуро), 5 файл.'''
        await update.message.reply_text(documents)
    elif text == "Список документов для бакалавриата":
        documents = '''Список документов для приемной комиссии:
1. Заявление о зачислении (заполняется в приемной комиссии).
2. Документ об образовании с приложением (подлинник).
3. Свидетельство о присуждении образовательного гранта (при наличии).
4. Сертификат ЕНТ или КТ.
5. 6 фотокарточек размером 3х4.
6. Медицинская справка формы 075/у со снимком флюорографии.
7. Копия прививочной карты (форма 063).
8. Копия документа, удостоверяющего личность – 3шт.
9. Копия приписного свидетельства или военного билета (для парней).
10. Копия трудовой книжки (при наличии).
11. Для формирования личного дела: скоросшиватель, картонный конверт (евро), 5 файлов.'''
        await update.message.reply_text(documents)
    elif text == "List of Documents for Bachelor's degree":
        documents = '''List of documents for the admissions committee:
1. Application for admission (to be filled out at the admissions office).
2. Document of education with an appendix (original).
3. Certificate of the award of an educational grant (if any).
4. UNT or CT certificate.
5. 6 pcs 3x4 photo cards.
6. Medical certificate form 075 with X-ray.
7. Copy of the vaccination card (form 063).
8. A copy of the identity document – 3 pcs.
9. A copy of the registration certificate or military ID (for guys).
10. A copy of the work record (if any).
11. To form a personal file: a folder, a cardboard envelope, 5 files.'''
        await update.message.reply_text(documents)
    elif text == "Магистратура деңгейіне құжаттар тізімі":
        documents = '''Қабылдау комиссиясына арналған құжаттар тізімі:
1. Қабылдау туралы өтініш (қабылдау комиссиясында толтырылады).
2. Қосымшасы бар білім туралы құжат (түпнұсқа).
3. Білім беру грантын беру туралы куәлік (бар болса).
4. ҰБТ немесе КТ сертификаты.
5. 3х4 өлшемді 6 фотокарта.
6. Флюорография суреті бар 075/Е нысанындағы медициналық анықтама.
7. Егу картасының көшірмесі (063-нысан).
8. Жеке басын куәландыратын құжаттың көшірмесі-3 дана.
9. Тіркеу куәлігінің немесе әскери билеттің көшірмесі (жігіттер үшін).
10. Еңбек кітапшасының көшірмесі (бар болса).
11. Жеке істі қалыптастыру үшін: құжат тігілетін мұқаба, картон конверт(Еуро), 5 файл.
'''
        await update.message.reply_text(documents)
    elif text == "Список документов для магистратуры":
        documents = '''Список документов для приемной комиссии:
1. Заявление о зачислении (заполняется в приемной комиссии).
2. Документ об образовании с приложением (подлинник).
3. Свидетельство о присуждении образовательного гранта (при наличии).
4. Сертификат ЕНТ или КТ.
5. 6 фотокарточек размером 3х4.
6. Медицинская справка формы 075/у со снимком флюорографии.
7. Копия прививочной карты (форма 063).
8. Копия документа, удостоверяющего личность – 3шт.
9. Копия приписного свидетельства или военного билета (для парней).
10. Копия трудовой книжки (при наличии).
11. Для формирования личного дела: скоросшиватель, картонный конверт (евро), 5 файлов.
'''
        await update.message.reply_text(documents)
    elif text == "List of Documents for Masters's degree":
        documents = '''List of documents for the admissions committee:
1. Application for admission (to be filled out at the admissions office).
2. Document of education with an appendix (original).
3. Certificate of the award of an educational grant (if any).
4. UNT or CT certificate.
5. 6 pcs 3x4 photo cards.
6. Medical certificate form 075 with X-ray.
7. Copy of the vaccination card (form 063).
8. A copy of the identity document – 3 pcs.
9. A copy of the registration certificate or military ID (for guys).
10. A copy of the work record (if any).
11. To form a personal file: a folder, a cardboard envelope, 5 files.
'''
        await update.message.reply_text(documents)
    elif text == "Докторантура деңгейіне құжаттар тізімі":
        documents = '''
Докторантураға түсуші адамдар мынадай құжаттар топтамасын ЖЖОКБҰға тапсырады:
1\) еркін нысандағы өтініш;
2\) білім туралы құжат \(құжаттарды қабылдау комиссиясына тапсырған кездегі түпнұсқасы\);
3\) жеке басын куәландыратын құжат \(жеке басын сәйкестендіру үшін қажет\);
4\) шет тілін меңгеруін растайтын электрондық сертификат \(ағылшын, неміс, француз\) ағылшын тілі: 
    IELTS   Academic\/International English Language Tests System Academic шекті балл \– кемінде 5,5;
    Test of English as a Foreign Language Institutional Testing Programm Internet\-based Test \(TOEFL IBT\), шекті балл \– кемінде 46\);
    Test of English as a Foreign Language Paper\-based testing \(TOEFL PBT\) шекті балл \– кемінде 453;
    неміс тілі: Deutsche Sprachpruеfung fuеr den Hochschulzugang \(DSH, Niveau В2\/В2 деңгейі\), TestDaF\-Prufung \(Niveau В2\/В2 деңгейі\);
    француз тілі: Test de Franзais International™ \(TFI \– оқу және тыңдалым секциялары бойынша B1 деңгейден төмен емес\), Diplome d\’Etudes en Langue franзaise \(DELF, B2 деңгейі\), Diplome Approfondi de Langue franзaise \(DALF, C1 деңгейі\), Test de connaissance du franзais \(TCF \– кемінде 50 балл\)\.
5\) \№ ҚР ДСМ\-175\/2020 бұйрықпен бекітілген 075\/у нысаны бойынша электрондық форматтағы медициналық анықтама\. Белгілі бір аумақта шектеу іс\-шаралары жүзеге асырылған, төтенше жағдай енгізілген, әлеуметтік, табиғи және техногендік сипаттағы төтенше жағдайлар туындаған жағдайларда осы іс\-шаралардың алынуына қарай тікелей білім беру ұйымдарына медициналық анықтама ұсынады\.
6\) 3x4 сантиметр көлеміндегі алты фотосурет;
7\) жұмыс орны бойынша кадр қызметімен расталған кадрларды есепке алу жөніндегі жеке іс парағы немесе еңбек қызметін растайтын өзге құжат;
8\) соңғы 3 күнтізбелік жылдағы ғылыми және ғылыми\-әдістемелік жұмыстардың тізімі \(ғылыми жарияланымдар, зерттеулер жүргізу жоспары, эссе және басқа құжаттар\);
9\) алдын ала іріктеу нәтижелері \(«Денсаулық сақтау» білім саласы бойынша\)\. 4\) және 7\) тармақшаларда көрсетілген құжаттардың түпнұсқалары мен көшірмелері түрінде ұсынылады, оларды салыстырғаннан кейін түпнұсқалар өтініш берушіге қайтарылады\.

Осы тармақта көрсетілген құжаттар тізбесін толық ұсынбаған кезде қабылдау комиссиясы түсушілерден құжаттарды қабылдамайды\.
Ұсынылатын сертификаттардың түпнұсқалығын және жарамдылық мерзімін ЖЖОКБҰның қабылдау комиссиялары тексереді\.
Докторантураға "магистр" дәрежесі және кемінде 9 ай еңбек өтілі бар немесе медицина мамандықтары бойынша резидентурада оқу бітірген адамдар қабылданады\.
[Қосымша ақпарат үшін](https://sites.google.com/tttu.edu.kz/tttu-edu/докторантура?authuser=0)
'''
        await update.message.reply_markdown_v2(documents, disable_web_page_preview=True)
    elif text == "Список документов для докторантуры":
        documents = '''Список документов для приемной комиссии:
1) заявление в произвольной форме;
2) документ об образовании (подлинник, при подаче документов в приемную комиссию);
3) документ, удостоверяющий личность (требуется для идентификации личности);
4) электронный сертификат, подтверждающий владение иностранным языком (английский, немецкий, французский) по программам
английский язык:
    IELTS Academic (АЙЛТС Академик)/International English Language Tests System Academic (Интернашнал Инглиш Лангудж Тестс Систем Академик) пороговый балл – не менее 5,5;  
    Test of English as a Foreign Language Institutional Testing Programm (Тест ов Инглиш аз а Форин Лангудж Инститьюшнал Тестинг програм) Internet-based Test (Интернет бейзид тест) (TOEFL IBT (ТОЙФЛ АйБИиТи), пороговый балл – не менее 46;
    TOEFL PBT (Тест ов Инглиш аз а Форин Лангудж пэйпер бэйсед тэстинг) Test of English as a Foreign Language Paper-based testing, пороговый балл – не менее 453;
немецкий язык: Deutsche Sprachpruеfung fuеr den Hochschulzugang (дойче щпрахпрюфун фюр дейн хохшулцуган) (DSH, NiveauВ2/уровень В2), TestDaF-Prufung (тестдаф-прюфун) (Niveau В2/уровень В2);
французский язык: Test de Franзais International™ – Тест де франсэ Интернасиональ (TFI (ТФИ) – не ниже уровня В2 по секциям чтения и аудирования), Diplome d’Etudes en Langue franзaise – Диплом дэтюд ан Ланг франсэз (DELF (ДЭЛФ), уровень B2), Diplome Approfondi de Langue franзaise – Диплом Аппрофонди де Ланг Франсэз (DALF (ДАЛФ), уровень В2), Test de connaissance du franзais – Тест де коннэссанс дю франсэ (TCF (ТСФ) – не менее 50 баллов).
5) медицинскую справку по форме 075/у в электронном формате, утвержденную приказом № ҚР ДСМ-175/2020). В случаях осуществления ограничительных мероприятий, введения чрезвычайного положения, возникновения чрезвычайных ситуаций социального, природного и техногенного характера на определенной территории предоставляют непосредственно в организации образования медицинскую справку по мере снятия данных мероприятий;
6) шесть фотографий размером 3x4 сантиметра;
7) личный листок по учету кадров или иной документ, подтверждающий трудовую деятельность, заверенный кадровой службой по месту работы;
8) список научных и научно-методических работ (научные публикации, план проведения исследований, эссе и другие документы) за последние 3 календарных года;
9) результаты предварительного отбора (по области образования «Здравоохранение»).

Документы, перечисленные в подпунктах 4) и 7), предоставляются в подлинниках и копиях, после сверки которых подлинники возвращаются заявителю.
'''
        await update.message.reply_text(documents)
    elif text == "List of Documents for Doctor's degree":
        documents = '''List of documents for the admissions committee:
1) an application in any form;
2) a document of education (original, when submitting documents to the admissions committee);
3) an identity document (required for identification);
4) electronic certificate confirming proficiency in a foreign language (English, German, French) according to the programs
English language:
    IELTS Academic/International English Language Tests System Academic (International English Language Tests Systems Academic) threshold score – at least 5.0;  
    Test of English as a Foreign Language Institutional Testing Program Internet-based Test (TOEFL IBT (TOEFL IQ), threshold score – at least 40;
    TOEFL PBT (Test of English as a Foreign Language Paper-based testing), the threshold score is at least 453;
German: Deutsche Sprachpruefung fuer den Hochschulzugang (Deutsche Sprachpruefung fuer dane hochschulzugan) (DSH, Niveau2/level B2), TestDaF-Prufung (TestDaF-prufung) (Niveau B2/level B2);
French: Test de Français International™ – Test de francais Internacional (TFI (TFI) – not lower than level B2 in reading and listening sections), Diplome d'Etudes en Langue française – Diploma of study en Lang francaise (DELF, level B2), Diplome Approfondi de Langue française – Diploma of Approfondi de Lang Francais (DALF, level B2), Test de connaissance du français – Test de connaissance du francais (TCF – at least 50 points).
5) a medical certificate in the form 075/y in electronic format, approved by order No. KR DSM-175/2020). In cases of restrictive measures, the introduction of a state of emergency, the occurrence of social, natural and man-made emergencies in a certain territory, a medical certificate is provided directly to the educational organization as these measures are lifted;
6) six photos measuring 3x4 centimeters;
7) a personal personnel record sheet or other document confirming employment, certified by the personnel service at the place of work;
8) a list of scientific and methodological works (scientific publications, research plan, essays and other documents) for the last 3 calendar years;
9) the results of the preliminary selection (in the field of education "Healthcare").

The documents listed in subparagraphs 4) and 7) are provided in originals and copies, after verification of which the originals are returned to the applicant.
'''
        await update.message.reply_text(documents)
    
    elif text in ['📄 Документы для участия в конкурсе грантов', '📄 Грантқа қатысу үшін қажетті құжаттар тізімі', '📄 Documents for participation in the grant competition']:
        if text == '📄 Грантқа қатысу үшін қажетті құжаттар тізімі':
            documents_grant = '''
📆Грант конкурсына құжаттар қабылдау 13-20 шілде аралығында, Ақмола, Ақтөбе, Атырау, Батыс Қазақстан, Қостанай, Солтүстік Қазақстан облыстарының талапкерлері үшін 13-24 шілде аралығында жүзеге асырылады.

🗂Құжаттарды жоғары оқу орындарының қабылдау комиссиялары арқылы офлайн және eGov арқылы онлайн тапсыруға болады.

❓ҰБТ-дан кейін грант конкурсына қатысу үшін қандай құжаттарды тапсыру керек?

Сақтап алыңыздар👇
🎓жеке куәлік;
🎓ҰБТ сертификаты;
🎓3х4 көлеміндегі фото;
🎓орта білім туралы аттестат (колледж түлектері үшін диплом);
🎓жеңілдетілген санат бойынша конкурсқа қатысу үшін растайтын құжаттар;
'''
            await update.message.reply_text(documents_grant)  
        elif text == '📄 Документы для участия в конкурсе грантов':
            documents_grant = '''
📆Прием документов в конкурсе грантов будет осуществляться с 13 по 20 июля, а для абитуриентов Акмолинской, Актюбинской, Атырауской, Западно-Казахстанской, Костанайской, Северо-Казахстанской областей - с 13 по 24 июля.

🗂Документы можно подать офлайн через приемные комиссии вузов и онлайн через eGov.

❓Какие документы нужно подать для участия в конкурсе грантов?

Не забудьте сохранить себе👇
🎓удостоверение личности;
🎓сертификат ЕНТ;
🎓фото размером 3х4;
🎓аттестат о среднем образовании (диплом для выпускников колледжей);
🎓подтверждающие документы для участия в конкурсе по льготной категории;'''
            await update.message.reply_text(documents_grant)
        elif text == '📄 Documents for participation in the grant competition':
            await update.message.reply_text('Sorry, for now, we cannot provide this information in english')

    elif text in ['🖊️ Information about grants', "🖊️ Информация о конкурсе грантов", "🖊️ Грант байқауы туралы ақпарат"]:
        if text == '🖊️ Information about grants':
            sorry = '''Sorry, for now we cannot provide this information '''
            await update.message.reply_text(sorry)
        elif text == "🖊️ Информация о конкурсе грантов":
            programs_keyboard = [['📄 Документы для участия в конкурсе грантов'], ['🎓 Льготные категории'], ['↩️ Назад в меню']]
            await update.message.reply_text("Выберите из меню",
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
        elif text == "🖊️ Грант байқауы туралы ақпарат":
            programs_keyboard = [['📄 Грантқа қатысу үшін қажетті құжаттар тізімі'], ['🎓 Жеңілдетілген санақ'], ['↩️ Назад в меню']]
            await update.message.reply_text("Мәзірдең таңдаңыз",
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )

    elif text in ['🎓 Льготные категории', '🎓 Жеңілдетілген санақ']:
        if text == '🎓 Льготные категории':
            kvota = '''
1.	Для граждан из числа лиц с инвалидностью первой или второй группы, лиц с инвалидностью с детства, детей с инвалидностью (1%)

2.	Для ветеранов боевых действий на территории других государств, ветеранов, приравненных по льготам к ветеранам Великой Отечественной войны (0,5%)

3.	Граждан из числа сельской молодежи на обучение по образовательным программам, определяющим социально-экономическое развитие села - сельская квота (35%)

4.	Для лиц казахской национальности, не являющихся гражданами Республики Казахстан (4%)

5.	Для детей-сирот и детей, оставшихся без попечения родителей, а также граждан РК из числа молодежи, потерявших или оставшихся без попечения родителей до совершеннолетия (1%)

6.	Граждан Республики Казахстан из числа сельской молодежи, переселяющихся в регионы, определенные правительством Республики Казахстан - серпін (5%)

7.	Для детей из семей, в которых воспитывается четыре и более несовершеннолетних детей (5%)

8.	Для детей из числа неполных семей, имеющих данный статус не менее трех лет (1%)

9.	Для детей из семей, воспитывающих детей с инвалидностью с детства, лиц с инвалидностью первой или второй группы (1%)
'''
            await update.message.reply_text(kvota)
        elif text == '🎓 Жеңілдетілген санақ':
            kvota = '''
1.	Бірінші немесе екінші топтаты мүгедектігі бар адамдар, бала кезінен мүгедектігі бар адамдар, мүгедектігі бар балалар арасынан шыққан азаматтар үшін (1%)

2.	Басқа мемлекеттердін аумағындаты ұрыс қимылдарынын ардагерлері, жеңілдіктер бойынша Ұлы Отан соғысынын ардагерлеріне теңестірілген ардагерлер үшін (0,5%)

3.	Ауылдын әлеуметтік-экономикалық дамуын айқындайтын білім беру бағдарламалары бойынша оқуға ауыл жастары арасынан шыққан азаматтар үшін - ауыл квотасы (35%)

4.	Қазакстан Республикасынын азаматтары болып табылмайтын ұлты қазақ адамдар үшін (4%)

5.	Жетім балалар және ата-аналарының қамқорлығынсыз қалған, сондай-ақ кәмелеттік жасқа толғанға дейін ата-анасынан айырылған немесе ата-анасының қамқорлығынсыз қалған жастар қатарындағы Қазақстан Республикасының азаматтары үшін(1%)

6.	Қазақстан Республикасының үкіметі айқындаған өңірлерге қоныс аударған ауыл жастары арасынан шыққан Қазақстан Республикасынын азаматтары үшін - серпін (5%)

7.	Кәмелетке толмаған төрт және одан көп бала тәрбиелеп отырған отбасылардағы балалар үшін (5%)

8.	Кемінде үш жыл толық емес отбасы мәртебесі бар отбасылардағы балалар үшін (1%)

9.	Бала кезінен мүгедектігі бар балаларды, бірінші немесе екінші топтағы мүгедектігі бар адамдарды тәрбиелеп отырған отбасылардағы балалар үшін (1%)
'''
            await update.message.reply_text(kvota)

    elif text in ['📘 Образовательные программы', '📘 Оқу бағдарламалары', '📘 Educational Programs']:
        if text == '📘 Образовательные программы':
            programs_keyboard = [['🎓 Бакалавриат'], ['🎓 Магистратура'], ['🎓 Докторантура'], ['↩️ Назад в меню']]
            await update.message.reply_text(
                'Выберите уровень образовательной программы:',
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
        elif text == '📘 Оқу бағдарламалары':
            programs_keyboard = [['🎓 Бакалавриат деңгейі'], ['🎓 Магистратура деңгейі'], ['🎓 Докторантура деңгейі'], ['↩️ Мәзірге оралу']]
            await update.message.reply_text(
                'Білім беру бағдарламасының деңгейін таңдаңыз:',
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
        elif text == '📘 Educational Programs':
            programs_keyboard = [["🎓 Bachelor's degree"], ["🎓 Master's degree"], ["🎓 Doctor's degree"], ['↩️ Back to the menu']]
            await update.message.reply_text(
                'Select the level of the educational program:',
                reply_markup=ReplyKeyboardMarkup(programs_keyboard)
            )
    
    elif text == '🌐 Тілді ауыстыру/Change language/Поменять язык':
        await change_language(update, context)
    
    elif text in ['🌟 Преимущества нашего университета', '🌟 Advantages of our university', '🌟 Біздің университеттің артықшылықтары']:
        if text == "🌟 Біздің университеттің артықшылықтары":
            advantages = '''Біздің университеттің артықшылықтары:

🏢 Барлық 4 оқу жылына арналған жатақхана 
Айына тек 4000 тг.

🎓 Көптеген гранттар  
Білім беру бағдарламалары мен университеттер бойынша мол гранттар.

🔬 Заманауи зертханалар  
Заманауи оқу-ғылыми зертханалық база.

🏭 Өнеркәсіппен тығыз ынтымақтастық  
ҚР ірі өнеркәсіптік кәсіпорындарымен тығыз ынтымақтастық, өндірістік практика және жұмысқа орналастыру.

💼 Жұмысқа орналасу деңгейі  
Біздің студентткрдің 90%-ы жұмысқа орналасады.

🎨 Шығармашылықты дамыту  
Шығармашылық тұлғаны дамыту шарттары: тегін спорт секциялары, тренажер залы, шығармашылық үйірмелер, пікірсайыс клубы, тренингтер және тағы басқалар.

💳 Икемді төлем жүйесі  
Оқу ақысын төлеудің икемді жүйесі.

🎖️ Университет гранттары  
Талантты белсенді студенттерге жыл сайын университет гранттарын бөлу.

🏠 Жатақханамен қамтамасыз ету  
Студенттердің жатақханамен 100% қамтамасыз етілуі.

🌏 Халықаралық байланыстар  
Германия, Польша, Чехия, Қытай, Ресей, Түркия және басқа елдермен кең халықаралық байланыстар.

🌐 Академиялық ұтқырлық  
Қазақстанның және жақын, алыс шетелдердің басқа жоғары оқу орындарында оқу және тағылымдамадан өту мүмкіндігі.'''
            await update.message.reply_text(advantages)
        elif text == "🌟 Advantages of our university":
            advantages = '''Advantages of Our University:

🏢 Dormitory for 4 Years
Affordable housing at just 4000 KZT per month.

🎓 Abundant Grants
Plenty of grants for various educational programs and universities.

🔬 Modern Facilities
State-of-the-art educational and scientific laboratories.

🏭 Industry Connections
Strong partnerships with leading industrial enterprises in Kazakhstan for internships and job placements.

💼 High Employment Rate
90% of our graduates secure employment.

🎨 Creative Development
Opportunities to nurture your creativity with free sports sections, a gym, creative circles, a debate club, trainings, and much more.

💳 Flexible Payment
Flexible tuition payment options to suit your needs.

🎖️ University Grants
Annual university grants for talented and active students.

🏠 Guaranteed Housing
100% dormitory provision for all students.

🌏 International Relations
Extensive partnerships with universities in Germany, Poland, Czech Republic, China, Russia, Turkey, and more.

🌐 Academic Mobility
Opportunities to study and complete internships at other universities in Kazakhstan and abroad through academic mobility programs.'''        
            await update.message.reply_text(advantages)
        elif text == "🌟 Преимущества нашего университета":
            advantages = '''Преимущества нашего университета:

🏢 Общежитие на все 4 года обучения  
Только 4000 тг в месяц.

🎓 Много грантов  
Широкий выбор грантов по образовательным программам и университетам.

🔬 Современные лаборатории  
Наличие современной учебно-научной лабораторной базы.

🏭 Тесное сотрудничество с промышленностью  
Сотрудничество с крупнейшими промышленными предприятиями РК для прохождения практик и трудоустройства выпускников.

💼 Высокий уровень трудоустройства  
90% наших выпускников находят работу.

🎨 Развитие творческой личности  
Условия для развития: бесплатные спортивные секции, тренажерный зал, творческие кружки, дебатный клуб, тренинги и многое другое.

💳 Гибкая система оплаты  
Гибкая система оплаты обучения.

🎖️ Университетские гранты  
Ежегодное выделение грантов для талантливых и активных студентов.

🏠 Гарантированное общежитие  
100% обеспеченность студентов общежитием.

🌏 Международные связи  
Широкие международные связи с университетами Германии, Польши, Чехии, Китая, России, Турции и других стран.

🌐 Академическая мобильность  
Возможность обучения и прохождения стажировок в других ВУЗах Казахстана, ближнего и дальнего зарубежья по программам академической мобильности.'''
            await update.message.reply_text(advantages)
    
    elif text in ['❓ Басқа сұрақ', '❓ Другой вопрос', '❓ Other Question']:
        if text == '❓ Другой вопрос':
            other_questions = '''
Напишите приемной комиссии на WhatsApp: 
Баймагамбетова Алтынай Хамитовна
8(701) 430 64 14, 
8(700) 569 06 47 '''
            await update.message.reply_text(other_questions)
        elif text == '❓ Басқа сұрақ':
            other_questions = '''
Қабылдау комиссиясының WhatsApp нөміріне жазыңыз: 
Баймагамбетова Алтынай Хамитовна
8(701) 430 64 14, 
8(700) 569 06 47 '''
            await update.message.reply_text(other_questions)
        elif text == '❓ Other Question':
            other_questions = '''
Please write to WhatsApp of Addmissions Committee: 
Baimagambetova Altynai Hamitovna
8(701) 430 64 14, 
8(700) 569 06 47 '''
            await update.message.reply_text(other_questions)
    
    elif text in ['↩️ Назад в меню', '↩️ Мәзірге оралу', '↩️ Back to the menu']:
        await send_main_menu(update, context)
    
    elif text in ['🎓 Бакалавриат', "🎓 Бакалавриат деңгейі", "🎓 Bachelor's degree"]:
        if text == "🎓 Бакалавриат":
            subjects_keyboard = [['📐Математика/💻информатика'], ['📐Математика/⚛️физика'], ['🧪Химия/⚛️физика'], ['🧪Химия/🧬биология'], ['📐Математика/🗺️география'], ['↩️ Назад']]
            await update.message.reply_text(
                'Выберите предметы:',
                reply_markup=ReplyKeyboardMarkup(subjects_keyboard)
            )
        elif text == "🎓 Бакалавриат деңгейі":
            subjects_keyboard = [['📐Математика мен 💻информатика'], ['📐Математика мен ⚛️физика'], ['🧪Химия мен ⚛️физика'], ['🧪Химия мен 🧬биология'], ['📐Математика мен 🗺️география'], ['↩️ Артқа']]
            await update.message.reply_text(
                'Пәндерді таңдаңыз:',
                reply_markup=ReplyKeyboardMarkup(subjects_keyboard)
            )
        elif text == "🎓 Bachelor's degree":
            subjects_keyboard = [['📐Math/💻ICT'], ['📐Math/⚛️Physics'], ['🧪Chemistry/⚛️Physics'], ['🧪Chemistry/🧬Biology'], ['📐Math/🗺️Geography'], ['↩️ Go back']]
            await update.message.reply_text(
                'Choose the subjects:',
                reply_markup=ReplyKeyboardMarkup(subjects_keyboard)
            )
    elif text in ['↩️ Назад', '↩️ Артқа', '↩️ Go back']:
        await send_main_menu(update, context)
    elif text in ['📐Математика/💻информатика', '📐Математика мен 💻информатика', '📐Math/💻ICT']:
        if text == '📐Математика/💻информатика':
            math_ict = '''Бакалавриат\(Математика\/информатика\):
    1\. [Программная инженерия](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/программная-инженерия?authuser=0)
    2\. [Технологии искусственного интеллекта](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/технология-искусственного-интеллекта?authuser=0)
    '''
            await update.message.reply_markdown_v2(math_ict, disable_web_page_preview=True)
        elif text == '📐Математика мен 💻информатика':
            math_ict = '''Бакалавриат\(Математика мен информатика\):
    1\. [Бағдарламалық инженерия](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/бағдарламалық-инженерия?authuser=2)
    2\. [Жасанды интеллект технологиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/жасанды-интеллект-технологиясы?authuser=2) 
    '''
            await update.message.reply_markdown_v2(math_ict, disable_web_page_preview=True)
        elif text == '📐Math/💻ICT':
            math_ict = '''Bachelor\(Math\/ICT\):
    1\. [Software Engineering](https://drive.google.com/file/d/1l04XfBWd-wLqwmeqfIY7ERtuSykiOwo9/view?usp=sharing)
    2\. [Artificial intelligence technologies](https://drive.google.com/file/d/17OIYek84PV-QQkubCtoyngqg4iVsQmXV/view?usp=sharing)
    '''
            await update.message.reply_markdown_v2(math_ict, disable_web_page_preview=True)
    elif text in ['📐Математика/⚛️физика', '📐Математика мен ⚛️физика', '📐Math/⚛️Physics']:
        if text == '📐Математика/⚛️физика':
            math_phys = '''Бакалавриат\(Математика\/физика\):
            1\.	[Материаловедение и технология новых материалов](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/материаловедение-и-технология-новых-материалов?authuser=0)
            2\.	[Энергообеспечение промышленных объектов](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/энергообеспечение-промышленных-объектов?authuser=0)
            3\.	[Теплоэнергетика промышленных предприятий и объектов жилищно\-коммунального хозяйства](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/теплоэнергетика-промышленных-предприятий-и-объектов-жил-комм-хозяйства?authuser=0)
            4\.	[Теплоэнергетика промышленных предприятий и объектов жилищно\-коммунального хозяйства \(на базе ТиПО\)](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/теплоэнергетика-промышленных-предприятий-и-объектов-жил-комм-хозяйства?authuser=0)
            5\.	[Инженерия систем автоматизации](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/инженерия-систем-автоматизации?authuser=0)
            6\.	[Технологическое оборудование промышленности](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/технологическое-оборудование-промышленности?authuser=0)
            7\.	[Кузнечно\-штамповочное производство в машиностроении](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/кузнечно-штамповочное-производство-в-машиностроение?authuser=0)
            8\.	[Транспортно\-технологические машины](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/транспортно-технологические-машины?authuser=0)
            9\.	[Автомобилестроение]()
            10\. [Обработка материалов давлением](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/обработка-материалов-давлением?authuser=0)
            11\. [Металлургия черных металлов](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/металлургия-черных-металлов?authuser=0)
            12\. [Металлургия цветных металлов](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/металлургия-цветных-металлов?authuser=0)
            13\. [Обогащение полезных ископаемых](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/обогащение-полезных-ископаемых?authuser=0)
            14\. [Проектный менеджмент в горно\-металлургической промышленности \(1\)]()
            15\. [Металлургия цветных металлов \(на базе ТиПО\)](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/металлургия-цветных-металлов?authuser=0)
            16\. [Металлургия черных металлов \(на базе ТиПО\)](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/металлургия-черных-металлов?authuser=0)
            17\. [Промышленное и гражданское строительство](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/промышленное-и-гражданское-строительство?authuser=0)
            18\. [Стандартизация, метрология и сертификация](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/стандартизация-метрология-и-сертификация?authuser=0)
            19\. [Промышленная, экологическая и пожарная безопасность](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/промышленная-экологическая-и-пожарная-безопасность?authuser=0)'''
            await update.message.reply_markdown_v2(math_phys, disable_web_page_preview=True)
        elif text == '📐Математика мен ⚛️физика':
            math_phys = '''Бакалавриат\(Математика мен физика\):
            1\. [Материалтану жəне жаңа материалдар технологиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/материалтану-және-жаңа-материалдар-технологиясы?authuser=2) 
            2\. [Өнеркəсiптiк нысандарды энергиямен қамтамасыздандыру](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/өнеркәсіптік-объектілерді-энергиямен-қамтамасыз-ету?authuser=2)
            3\. [Өнеркəсiптiк кəсiпорындардың жəне тұрғын үй коммуналдық шаруашылығының нысандарының жылуэнергетикасы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/өнеркәсіптік-кәсіпорындардың-және-тұрғын-үй-коммуналдық-шаруашылығының-ныса?authuser=2)
            4\. [Өнеркəсiптiк кəсiпорындардың жəне тұрғын үй коммуналдық шаруашылығының нысандарының жылуэнергетикасы \(ТжКБ негiзiнде\)](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/өнеркәсіптік-кәсіпорындардың-және-тұрғын-үй-коммуналдық-шаруашылығының-ныса?authuser=2)
            5\. [Автоматтандыру жүйесiнiң инженериясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/автоматтандыру-жүйесінің-инженериясы?authuser=2) 
            6\. [Өндiрiстiң технологиялық жабдықтары](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/өндірістің-технологиялық-жабдықтары?authuser=2) 
            7\. [Машинажасаудағы ұсталық\-қалыптау өндiрiсi](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/машинажасаудағы-ұсталық-қалыптау-өндірісі?authuser=2)
            8\. [Көлiктiк\-технологиялық машиналар](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/көтеру-тасымалдаушы-құрылыс-және-жол-машиналары?authuser=2) 
            9\. [Көтеру\-тасымалдаушы, құрылыс және жол машиналары](https://drive.google.com/file/d/1yk4zp0qw62q41TCWGJgIEx40TlAWcmxm/view?usp=sharing)
            10\. [Материалдарды қысыммен өңдеу](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/материалдарды-қысыммен-өңдеу?authuser=2) 
            11\. [Қара металдар металлургиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/қара-металдар-металургиясы?authuser=2) 
            12\. [Түстi металдар металлургиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/түсті-металдар-металургиясы?authuser=2) 
            13\. [Пайдалы қазбаларды байыту](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/пайдалы-қазбаларды-байыту?authuser=2)
            14\. Тау\-кен металлургия өнеркəсiбiндегi жобалық менеджмент \(1\)
            15\. [Түстi металдар металлургиясы \(ТжКБ негiзiнде\)](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/түсті-металдар-металургиясы?authuser=2) 
            16\. [Қара металдар металлургиясы \(ТжКБ негiзiнде\)](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/қара-металдар-металургиясы?authuser=2) 
            17\. [Өнеркəсiптiк жəне азаматтық құрылыс](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/өнеркәсіптік-және-азаматтық-құрылыс?authuser=2) 
            18\. [Стандарттау, метрология жəне сертификаттау](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/стандарттау-метрология-және-сертификаттау?authuser=2) 
            19\. [Өндiрiстiк, экологиялық жəне өрт қауiпсiздiгi](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/өндірістік-экологиялық-және-өрт-қауіпсіздігі?authuser=2)'''
            await update.message.reply_markdown_v2(math_phys, disable_web_page_preview=True)
        elif text == '📐Math/⚛️Physics':
            math_phys = '''Bachelor\(Math\/Physics\):
            1\. [Materials science and technology of new materials](https://drive.google.com/file/d/1MIJi9LG9weeNprEz2VF-Sr-C3G6l8vZy/view?usp=sharing)
            2\. [Energy supply of industrial facilities](https://drive.google.com/file/d/1fh-oFP7l7BMko0xpRmWsmiX-M8ja6vOT/view?usp=sharing)
            3\. [Heat power engineering of industrial companies and objectsof housing and communal services](https://drive.google.com/file/d/17A4uBKAHENNgKnHwrF3C3lrun8i89BCu/view?usp=sharing)
            4\. [Heat power engineering of industrial companies and objectsof housing and communal services \(based on TVET\)](https://drive.google.com/file/d/17A4uBKAHENNgKnHwrF3C3lrun8i89BCu/view?usp=sharing)
            5\. Engineering of automation systems
            6\. [Technological equipment of industry](https://drive.google.com/file/d/1rlloDLom6fa_c9s2jgsS_Nd1Tla1pDxS/view?usp=sharing)
            7\. [Forging\-stamping production in mechanical engineering](https://drive.google.com/file/d/1mvqcV2c0ZXc9VjhxK8OgO0ocKV7u94fB/view?usp=sharing)
            8\. [Transport and technological machines](https://drive.google.com/file/d/192g8zNyiRnTjRDoKOquOeeP5th4llcbL/view?usp=sharing)
            9\. [Lifting\-transport, building and road machines](https://drive.google.com/file/d/1OBu1AF-7ZzqdUooCys0DIxp9csbF9LBK/view?usp=sharing)
            10\. [Processing of materials by pressure](https://drive.google.com/file/d/1ADWVBKi0q4-1re4qDRyZiCdkLB21tyHS/view?usp=sharing)
            11\. [Metallurgy of ferrous metals](https://drive.google.com/file/d/1QQcx_Uz8LukyKGhKkG_rON8C84rdhaw-/view?usp=sharing)
            12\. [Metallurgy of non\-ferrous metals](https://drive.google.com/file/d/12LwfIUHQ0EaA3J_rSc-uZFPtOgFsx8VD/view?usp=sharing)
            13\. [Mineral processing](https://drive.google.com/file/d/1Gji8j3l24HKmmtnQq7jxLTdET3sHf21W/view?usp=sharing)
            14\. Project management in the mining and metallurgical industry \(1\)
            15\. [Metallurgy of non\-ferrous metals \(based on TPE\)](https://drive.google.com/file/d/12LwfIUHQ0EaA3J_rSc-uZFPtOgFsx8VD/view?usp=sharing)
            16\. [Metallurgy of ferrous metals \(based on TIPO\)](https://drive.google.com/file/d/1QQcx_Uz8LukyKGhKkG_rON8C84rdhaw-/view?usp=sharing)
            17\. [Industrial and civil engineering](https://drive.google.com/file/d/1b2F1eAOCXTB5Nn41toNXrFLaeWGjCghz/view?usp=sharing)
            18\. [Standardization, metrology and certification](https://drive.google.com/file/d/1QapVUSg56HENeXS6AK148_RAvBE68krH/view?usp=sharing)
            19\. [Industrial, environmental and fire safety](https://drive.google.com/file/d/1SUaNapcgRhaWkgldu2S_fbkZ4nvXIOOt/view?usp=sharing)'''
            await update.message.reply_markdown_v2(math_phys, disable_web_page_preview=True)
    elif text in ['🧪Химия/⚛️физика', '🧪Химия мен ⚛️физика', '🧪Chemistry/⚛️Physics']:
        if text == '🧪Химия/⚛️физика':
            chem_phys = '''Бакалавриат\(Химия\/физика\):
            1\. [Химическая технология органических веществ](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/химическая-технология-органических-веществ?authuser=0)'''
            await update.message.reply_markdown_v2(chem_phys, disable_web_page_preview=True)
        elif text == '🧪Химия мен ⚛️физика':
            chem_phys = '''Бакалавриат\(Химия мен физика\):
            1\. [Органикалық заттардың химиялық технологиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/органикалық-заттардың-химиялық-технологиясы?authuser=2)'''
            await update.message.reply_markdown_v2(chem_phys, disable_web_page_preview=True)
        elif text == '🧪Chemistry/⚛️Physics':
            chem_phys = '''Bachelor\(Chemistry\/Physics\):
            1\. [Chemical technology of organic substances](https://drive.google.com/file/d/1kTiKlB5W36og-Cx6ooL0SvyNnUdDuXTR/view?usp=sharing)'''
            await update.message.reply_markdown_v2(chem_phys, disable_web_page_preview=True)
    elif text in ['🧪Химия/🧬биология', '🧪Химия мен 🧬биология', '🧪Chemistry/🧬Biology']:
        if text == '🧪Химия/🧬биология':
            chem_bio = '''Бакалавриат\(Химия\/биология\):
            1\. [Технология фармацевтического производства](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/технология-фармацевтического-производства?authuser=0)'''
            await update.message.reply_markdown_v2(chem_bio, disable_web_page_preview=True)
        elif text == '🧪Химия мен 🧬биология':
            chem_bio = '''Бакалавриат\(Химия мен биология\):
            1\. [Фармацевтикалық өндiрiс технологиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/фармацевтикалық-өндіріс-технологиясы?authuser=2)'''
            await update.message.reply_markdown_v2(chem_bio, disable_web_page_preview=True)
        elif text == '🧪Chemistry/🧬Biology':
            chem_bio = '''Bachelor\(Chemistry\/Biology\):
            1\. [Pharmaceutical production technology](https://drive.google.com/file/d/13tEaUjKFMOJRjqwbEjbIpywPG9CeBZs8/view?usp=sharing)'''
            await update.message.reply_markdown_v2(chem_bio, disable_web_page_preview=True)
    elif text in ['📐Математика/🗺️география', '📐Математика мен 🗺️география', '📐Math/🗺️Geography']:
        if text == '📐Математика/🗺️география':
            math_geo = '''Бакалавриат\(Математика\/география\):
            1\.	[Менеджмент в сфере предпринимательства](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/менеджмент?authuser=0) 
            2\.	[Экономика бизнеса](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/экономика-бизнеса?authuser=0)
            3\.	[Учет и аудит в предпринимательстве](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/учет-и-аудит?authuser=0)
            4\. [Экономика финансовой организации](https://sites.google.com/tttu.edu.kz/abiturient/бакалавриат/экономика-финансовой-организации?authuser=0)'''
            await update.message.reply_markdown_v2(math_geo, disable_web_page_preview=True)
        elif text == '📐Математика мен 🗺️география':
            math_geo = '''Бакалавриат\(Математика мен география\):
            1\. [Кəсiпкерлiк саласындағы менеджментi](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/менеджмент?authuser=2) 
            2\. [Бизнес экономикасы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/бизнес-экономикасы?authuser=2)
            3\. [Кəсiпкерлiктегi есеп жəне аудит](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/есеп-және-аудит?authuser=2)
            4\. [Қаржы ұйымының экономикасы](https://sites.google.com/tttu.edu.kz/tttu-edu/бакалавриат/қаржы-ұйымының-экономикасы?authuser=2)'''
            await update.message.reply_markdown_v2(math_geo, disable_web_page_preview=True)
        elif text == '📐Math/🗺️Geography':
            math_geo = '''Bachelor\(Math\/Geography\):
            1\. [Management in the field of entrepreneurship](https://drive.google.com/file/d/13PIOz_iiKYCjkt_6VrSh-SVE63sMll8r/view?usp=sharing) 
            2\. [Business Economics](https://drive.google.com/file/d/1fHgKu6LKj89twv5Kp1lXGobwfOlxsfhB/view?usp=sharing)
            3\. [Accounting and auditing in entrepreneurship](https://drive.google.com/file/d/1nIkOjDJySNSZliZJ_ibqVjXkZDuaXMXb/view?usp=sharing)
            4\. [Economics of financial organization](https://drive.google.com/file/d/1Z1Ds6rM9KSq9yCU4KuM3AYyVU0b5kvZE/view?usp=sharing)'''
            await update.message.reply_markdown_v2(math_geo, disable_web_page_preview=True)
    
    elif text in ['🎓 Магистратура', '🎓 Магистратура деңгейі', "🎓 Master's degree"]:
        if text == "🎓 Магистратура":
            master_programs = '''[Магистратура](https://tttu.edu.kz/ru/obrazovanie/modulnie-obrazovatelnie-programmi/):
            1\.	Экономика 
            2\.	Автоматизация и управление
            3\.	Химическая технология органических веществ
            4\.	Материаловедение и нанотехнологии материалов
            5\.	Электроэнергетика
            6\.	Технология обработки новых конструкционных материалов
            7\.	Инжиниринг технологического оборудования
            8\.	Инжиниринг транспортно\-технологических систем
            9\.	Металлургия черных и цветных металлов
            10\. Технология фармацевтического производства
            11\. Теория и технология проектирования зданий и сооружений
            12\. Промышленная и экологическая безопасность'''
            await update.message.reply_markdown_v2(master_programs, disable_web_page_preview=True)
        elif text == "🎓 Магистратура деңгейі":
            master_programs = '''[Магистратура деңгейі](https://tttu.edu.kz/education/modulnie-obrazovatelnie-programmi/):
            1\. Экономика
            2\. Автоматтандыру жəне басқару
            3\. Органикалық заттардың химиялық технологиясы
            4\. Материалтану жəне материалдардың нанотехнологиясы
            5\. Электр энергетикасы
            6\. Жаңа конструкциялық материалдарды өңдеу технологиясы
            7\. Технологиялық жабдықтардың инжинирингi
            8\. Көлiктiк\-технологиялық жүйелер инжинирингi
            9\. Қара жəне түстi металдар металлургиясы 
            10\. Фармацевтикалық өндiрiс технологиясы
            11\. Ғимараттар мен құрылыстарды жобалау теориясы мен технологиясы
            12\. Өнеркəсiптiк жəне экологиялық қауiпсiздiк'''
            await update.message.reply_markdown_v2(master_programs, disable_web_page_preview=True)
        elif text == "🎓 Master's degree":
            master_programs = '''[Magistracy](https://tttu.edu.kz/en/modular-educational-programs/):
            1\. Economics 
            2\. Automation and control
            3\. Chemical technology of organic substances
            4\. Materials science and nanotechnology of materials
            5\. Electric power industry
            6\. Technology of processing new structural materials
            7\. Engineering of technological equipment
            8\. Engineering of transport and technological systems
            9\. Metallurgy of ferrous and non\-ferrous metals
            10\. Pharmaceutical production technology
            11\. Theory and technology of design of buildings and structures
            12\. Industrial and environmental safety'''
            await update.message.reply_markdown_v2(master_programs, disable_web_page_preview=True)
    
    elif text in ['🎓 Докторантура', '🎓 Докторантура деңгейі', "🎓 Doctor's degree"]:
        if text == "🎓 Докторантура":
            phd_programs = '''[Докторантура](https://tttu.edu.kz/ru/obrazovanie/modulnie-obrazovatelnie-programmi/):
            1\.	[Химическая технология органических веществ](https://sites.google.com/tttu.edu.kz/abiturient/докторантура/химическая-инженерия-и-процессы?authuser=0)
            2\.	[Автоматизация и управление](https://sites.google.com/tttu.edu.kz/abiturient/докторантура/автоматизация-и-управление?authuser=0)
            3\.	[Инновационный инжиниринг технологических машин](https://sites.google.com/tttu.edu.kz/abiturient/докторантура/инновационный-инжиниринг-технологических-машин?authuser=0)
            4\.	[Нанотехнологии и наноматериалы в инженерии](https://sites.google.com/tttu.edu.kz/abiturient/докторантура/нанотехнологии-и-наноматериалы-в-инженерии?authuser=0)
            5\.	[Металлургия черных и цветных металлов](https://sites.google.com/tttu.edu.kz/abiturient/докторантура/металлургия-черных-и-цветных-металлов?authuser=0)'''
            await update.message.reply_markdown_v2(phd_programs, disable_web_page_preview=True)
        elif text == "🎓 Докторантура деңгейі":
            phd_programs = '''[Докторантура деңгейі](https://tttu.edu.kz/education/modulnie-obrazovatelnie-programmi/):
            1\. [Органикалық заттардың химиялық инженериясы](https://sites.google.com/tttu.edu.kz/tttu-edu/докторантура/органикалық-заттардың-химиялық-технологиясы?authuser=0)
            2\. [Автоматтандыру жəне басқару](https://sites.google.com/tttu.edu.kz/tttu-edu/докторантура/автоматтандыру-және-басқару?authuser=0)
            3\. [Технологиялық машиналардың инновациялық инженериясы](https://sites.google.com/tttu.edu.kz/tttu-edu/докторантура/технологиялық-машиналардың-инновациялық-инжинирингі?authuser=0)
            4\. [Инженериядағы нанотехнология](https://sites.google.com/tttu.edu.kz/tttu-edu/докторантура/нанотехнологии-и-наноматериалы-в-инженерии?authuser=0)
            5\. [Қара жəне түстi металдар металлургиясы](https://sites.google.com/tttu.edu.kz/tttu-edu/докторантура/қара-және-түсті-металдар-металлургия?authuser=0)'''
            await update.message.reply_markdown_v2(phd_programs, disable_web_page_preview=True)
        elif text == "🎓 Doctor's degree":
            phd_programs = '''[Doctoral sudies](https://tttu.edu.kz/en/modular-educational-programs/):
            1\. Chemical technology of organic substances
            2\. Automation and control
            3\. Innovative engineering of technological machines
            4\. Nanotechnology in engineering
            5\. Metallurgy of ferrous and non\-ferrous metals'''
            await update.message.reply_markdown_v2(phd_programs, disable_web_page_preview=True)
    
    else:
        await update.message.reply_text('''
Кешіріңіз, мен әлі ондай сұрақтарға жауап бере алмаймын😢. Егер басқа сурақтарыңыз болса "Басқа сұрақ" пернесін басыңыз.
                                               
Извините, я ещё не могу ответить на такие вопросы😢. Если есть другие вопросы, нажмите на кнопку "Другой вопрос".

Sorry, I can't answer such questions now😢. If you have other questions, please press the button "Other Question".                                               
''')

# Функция обработки текстовых сообщений
async def text_message(update: Update, context: CallbackContext) -> None:
    language = context.user_data.get('language')
    if language is None:
        await choose_language(update, context)
    else:
        await main_menu(update, context)

if __name__ == '__main__':
    application = Application.builder().token('6979043777:AAE8wvIY7KMY-rPqGioeVH37IdsbLJe5v60').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))

    application.run_polling()
