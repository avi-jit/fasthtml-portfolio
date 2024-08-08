from fasthtml.fastapp import *
from fasthtml.common import *
import utils
import constants

def fun():
    name = constants.HEADING
    return Titled(
        utils.nav(constants.HEADING, constants.NAVDICT),
    P(
        'I love storytelling. My most popular',
        A('short film', href='https://www.youtube.com/watch?v=Uy_3XKqsJZk'),
        'has over 65,000 views on YouTube, which involved two whole years and the effort of 50+ volunteer cast and crew. My other productions include a',
        A('documentary on a World War 2 jet', href='https://www.facebook.com/fmc.iitbhu/videos/747155185437805/'),
        'and a',
        A('comedy sketch on how our college hotspot resembles Facebook-ing', href='https://www.facebook.com/fmc.iitbhu/videos/807030382783618/'),
        ', as well as a cute romantic film, that is yet to be compiled and released!'
    ),
    Iframe(width='560', height='315', src='https://www.youtube.com/embed/Uy_3XKqsJZk?si=yT0o9R52pvSWYUVs', title='YouTube video player', frameborder='0', allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share', referrerpolicy='strict-origin-when-cross-origin', allowfullscreen=''),
    P(
        'I also write articles, stories, newspapers,',
        A('blogs', href='https://thawani.notion.site'),
        ', songs & novels. Some of them are:'
    ),
    Ol(
        Li(
            Strong('Published Articles'),
            ': I have published in',
            A('The Print', href='https://theprint.in/campus-voice/will-panjshir-become-a-taiwan-afghanistans-story-matches-with-china/732849/'),
            'and',
            A('ISI News', href='https://www.isi.edu/news/38134/do-humans-trust-ai-coworkers/'),
            '.'
        ),
        Li(
            Strong('Sci-fi novel'),
            ': DNA Revolution, a story of Venezuela embroilled in a politico-military crisis on the eve of a major breakthrough in genetics.'
        ),
        Li(
            Strong('Short stories book'),
            ': Martyrs’ Horizon, inspired by a Chicken Soup book I read.'
        ),
        Li(
            Strong('Newspaper'),
            ': Articles for the college newsletter',
            A('Quest', href='https://issuu.com/thequest_iitbhu'),
            'at IIT BHU, and the school newsletter at City Montessori School'
        ),
        Li(
            Strong('Blogs'),
            ': I have some old ones on',
            A('Medium', href='https://medium.com/@avijitthawani'),
            'and many newer ones on',
            A('Notion', href='https://thawani.notion.site'),
            '.'
        )
    ),
    P('I’ve also participated in festival management, street plays, skits, dance clubs, robo-soccer, rap songs, stand-up comedy, handicrafts, and sketching.'),
    P(
        'I consider myself a lifelong learner and a big fan of',
        A('spaced repetition', href='https://ncase.me/remember'),
        '. I’ve enrolled in a wide range of classes like Interactive Journalism, Chinese History, Macroeconomics, Social Entrepreneurship, Self-Defense, Improv, Hip-Hop Dance, Cognitive Neuroscience, Film Appreciation, and African History.'
    ),
    P(
        'I’m an avid reader of books, both non-fiction and fiction. Currently loving Murakami. Trying to update my list on',
        A('Goodreads', href='https://www.goodreads.com/user/show/4791083-avijit-thawani'),
        '.'
    ),
    P('I have been fortunate enough to live in four countries and travel across the world. Some of the cities I’ve been to are (most recent first):'),
    Ul(
        Li('Europe: London, Berlin, Amsterdam, Utrecht, Florence, Pisa, Bruges, Dubrovnik, Dublin, Killarney, Galway, Cambridge'),
        Li('United States: Baltimore, New York, Philadelphia, Boston, Los Angeles, Santa Barbara, San Diego, San Francisco, Michigan, Pittsburgh'),
        Li('Asia: Beijing, Singapore, Kuala Lumpur, Seoul, Kathmandu, Tokyo'),
        Li('New Zealand: Auckland, Queenstown, Wanaka, Makarora'),
        Li('South India: Bangalore, Coorg, Pondicherry, Madras, Auroville, Rameshwaram'),
        Li('West India: Mumbai, Goa, Pune, Shirdi'),
        Li('East India: Puri, Kolkata'),
        Li('North India: Manali, Nainital, Dehradun, Haridwar, Hrishikesh, Shimla, Chandigarh'),
        Li('Central India: New Delhi, Lucknow, Varanasi, Allahabad, Agra, Dudhwa')
    ),
    Div(
        Div(
            Img(src='https://camo.githubusercontent.com/a0460bf797789392dd9e679625aef788be2f3ebfddaf5ddddbb02a48348ccabe/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d316f494e4a387142616972644937504e5a63774257426878374b5034624b507a34', alt='Big Sur'),
            Div('Big Sur, California', cls='carousel-caption'),
            style='display: block;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/0c47718658fbefe0ff4a9e54f77c13e4a86dc69aa46e29df0994ddcdc56314a3/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d317876684a6b6f6b3770316a756c3958323631656b4a7944682d5a6c346963496e', alt='platform 9 3/4'),
            Div("Off to Hogwarts (Platform 9 3/4 at King's Cross, London)", cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/a8be52297f941891b29ece888dee497a616018f0e49dc22af75a5c061ba841b4/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31376833476e50682d51513371456c3335716546523569426677746433466f437a', alt='Grand Canyon'),
            Div('Inside the Grand Canyon (Nevada, USA)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/15415c37afdfe04fec2767de69afedf66a73d6860a9157e750235e5fbf9633e8/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31515f35766264674f4c66575236706555743576475155544c4d6e756f46686334', alt='Dubrovnik'),
            Div("Inspecting the fortifications at King's Landing (Dubrovnik, Croatia)", cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/4d5e8853746e806fd85d885d2b472bec1b926fcc170d8cf334c7d9d7af2efdc8/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d314156616b4d3856743931597968386f46624a496741655f4750394f574d654942', alt='skydiving'),
            Div('Skydiving (Auckland, New Zealand)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/83fe3bc62a885bfff2c6fa5b74ec3b1c46a2b496f63dac351c8cb1023007ca26/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31765a645168486775337039386e303578517a497434386e4f6d6e746d33487745', alt='Unicorn'),
            Div('The closest thing to a unicorn on Earth (Ireland)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/39d9b8169a2a8cb0d4592a591da33069821f0a700cbe5e2c500708abdd6b7238/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31565649624c6443516c4d74313979527a75554947384f7073464433334c6d3650', alt='Shashi Tharoor'),
            Div('Book-signing with Dr Shashi Tharoor, an Indian politician (Cambridge, UK)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/b141b51b011d8bcdf2643368703e1e08d78b1357ecb7106235db51189fdb204d/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d316b30434f373473374c7934634751674d4f7768574f793862505f472d344c7265', alt='Lake District'),
            Div(
                'A French, a Brit, a Brazillian, an Indian, and a Turk walk into a',
                Del('bar'),
                'mountain (Lake District, UK)',
                cls='carousel-caption'
            ),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/a1b3c15960be8a5204dc3b54cca55934cdd1bdba64f78d56bb08b5485b354aa3/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d314d63566271702d524c474b4b4c4f6262756e2d346470743348424c756c4c4e64', alt='Redwood'),
            Div('Amidst the giant Redwoods (Northern California)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/ac8295001c1f4431c5bcb32ef2dad42b25f8eb5f22f316175916c03d8d155e29/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d315f477043714c3550307a4c52437076364a4b347931385375506e46716b5a4c4c', alt='westminster'),
            Div('Seat of the Inglorious Empire (Westminster, London)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        Div(
            Img(src='https://camo.githubusercontent.com/8561fb7d6e780dcf6450febbeb78618263a434cd3d2ca9e4770e92cc1d318738/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31776b6a5668324e61354f5a5f4144516572446572577472772d787a6967417549', alt='wanaka'),
            Div('The most beautifully placed tree on the planet (Wanaka Tree, New Zealand)', cls='carousel-caption'),
            style='display: none;',
            cls='carousel-slide'
        ),
        A('❮', onclick='moveSlide(-1)', cls='carousel-control left'),
        A('❯', onclick='moveSlide(1)', cls='carousel-control right'),
        cls='carousel-container'
    ),
    Style('.carousel-container {\r\n  width: 100%;\r\n  max-width: 600px;\r\n  position: relative;\r\n  margin: auto;\r\n}\r\n.carousel-slide {\r\n  display: none;\r\n  position: relative;\r\n  height: 400px; /* Fixed height */\r\n}\r\n.carousel-slide img {\r\n  width: 100%;\r\n  height: 100%;\r\n  object-fit: cover; /* Ensures image covers the slide area */\r\n}\r\n.carousel-caption {\r\n  position: absolute;\r\n  bottom: 8px;\r\n  left: 0;\r\n  width: 100%;\r\n  text-align: center;\r\n  color: white;\r\n  font-size: 20px;\r\n  padding: 8px;\r\n  background-color: rgba(0, 0, 0, 0.5);\r\n}\r\n.carousel-control {\r\n  position: absolute;\r\n  top: 50%;\r\n  transform: translateY(-50%);\r\n  cursor: pointer;\r\n  font-size: 24px;\r\n  color: white;\r\n  background-color: rgba(0,0,0,0.5);\r\n  padding: 10px;\r\n}\r\n.carousel-control.left {\r\n  left: 10px;\r\n}\r\n.carousel-control.right {\r\n  right: 10px;\r\n}'),
    Script('var slideIndex = 1;\r\nshowSlide(slideIndex);\r\n\r\nfunction moveSlide(n) {\r\n  showSlide(slideIndex += n);\r\n}\r\n\r\nfunction showSlide(n) {\r\n  var i;\r\n  var slides = document.getElementsByClassName("carousel-slide");\r\n  if (n > slides.length) {slideIndex = 1}    \r\n  if (n < 1) {slideIndex = slides.length}\r\n  for (i = 0; i < slides.length; i++) {\r\n      slides[i].style.display = "none";  \r\n  }\r\n  slides[slideIndex-1].style.display = "block";  \r\n}')
)