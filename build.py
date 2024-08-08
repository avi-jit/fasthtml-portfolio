from fasthtml.fastapp import *
from fasthtml.common import *
import utils
import constants

def build():
    name = constants.HEADING
    return Titled(
        utils.nav(constants.HEADING, constants.NAVDICT),
        #name, 
        P("Alongside my research, I have been building and releasing consumer products by leading a group of employees and hacking away on weekends.",
        "In addition to these self-driven products, I love helping startups build proof-of-concepts and streamline their AI/NLP-related projects, whether it be in mobility APIs or fintech. Please reach out if you wish to chat!"),
        Table(
    Tbody(
        Tr(
            Td('Product'),
            Td('Description')
        ),
        Tr(
            Td(
                Img(src='https://media.licdn.com/dms/image/D560BAQErolBif39Nxg/company-logo_200_200/0/1713706098061/pinegap_logo?e=2147483647&v=beta&t=k_Ak553Jpnx_sF3XjaMxreQ6jw1Ckd79iaNwHK-ErtA', alt='PineGap.ai', style='width:400px;')
            ),
            Td(
                A('PineGap.ai', href='https://www.pinegap.ai/'),
                'is a VC-backed startup that disrupts equity research with large language models and generative AI. As a founding MLE/LLM Engineer, I help finetune models, build RAG pipelines, custom evals, LangChains, and deploy these models in prod.'
            )
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/7f31909c60e3f674f318d20da78b988fce3fda866378932072fa9d4ad3e545e1/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d314a736231466b6556716a4b757a5135417a7865566e792d3375614179555f4c47', alt='Saras edtech chatbot', style='width:400px;')
            ),
            Td(
                A('Saras', href='https://t.me/saras_gpt_bot'),
                'is your personal AI tutor, that I developed as a Telegram chatbot and pitched at the New Venture Seed Contest (we won a $1500 grant) and the USC Trojan Tank (we stood third)!'
            )
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/e1585269cb5336e987712ae897c9df36814e77785e8f1e2be93e6da7f83766d9/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d3178594176646832554b4d51336c4a3566336e5378365975613674786963327045', alt='Ballpark', style='width:400px;')
            ),
            Td(
                'Harsh helped me make',
                A('Wordle for Numbers', href='https://ball-park.netlify.app'),
                '- a fun and informative game that lets you challenge your friends and improve your numeracy skills.'
            )
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/e4313c63dff24c463b2107d9c3b2e6e796dee53ea7c15ae55d61f2338084f1d0/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31336147373763677a61575974444d4b5f686a37504471525a553769303750364c', alt='Living Surveys', style='width:400px;')
            ),
            Td(
                'Eshaan helped me create',
                A('Living Surveys', href='https://github.com/EshaanAgg/Research-Literature-Manager'),
                ", an open source lit review tool that you can use to avoid FOMO in academia. We use Github Actions, Semantic Scholar, and Netlify to help you host your own living survey paper, with daily updated recommendations for new and relevant publications! Here's a",
                A('talk at ISI', href='https://youtu.be/FUIq9-lJ9ag?si=YjWr4ZFZjReJsEI2'),
                'presenting the tool.'
            )
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/fcfaf060aed88f08428033d0cc0906272d48c5f57aad36a9e8b2299f86380faf/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d314453727034736c645f6b755562766b394331464d4977766c66754e433066624d', alt='DesignAR', style='width:400px;')
            ),
            Td('Our Augmented Reality app was a national finalists and worldwide #6 at the Microsoft Imagine Cup 2016 and the Samsung VR Appathon. Out startup DesignAR received several VC funding offers.')
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/a5907bd4b03af5b728212f4b054c87c20ff9f2400fdfe9a48da457bc65761e70/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d3165373962677635503530496a726d58635a6e68376b3159574e5a6f7053493978', alt='Election Guide Interactive', style='width:400px;')
            ),
            Td(
                'I teamed up with journalists from the USC Annenberg Media Interactive Desk to narrate a',
                A('data story', href='https://annenberginteractives.com/2020-2021/voting-information-by-state/'),
                'on US 2020 Elections.'
            )
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/4f3a47cddc203cfdbcb209e1088b9875f84d59c4d41b02ad45d744571e1bad5a/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d31457534713534545a566d794f6d7871346f327066696e3654673671544e306943', alt='SUTD', style='width:400px;')
            ),
            Td('I was recruited in the Singapore Smart City Project to develop better sensors, so I also volunteered to model the incoming weather data from across the country with machine learning to make predictions.')
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/40f4d639bbd2094c401a4ef828d410ca30158e4d1c819bbe1c87cf6684493cec/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d315979666b6c4272614e694777453950657774554e6e77647677444d3839545959', alt='Covid', style='width:400px;')
            ),
            Td(
                'Covid-19 brought tragic times in India. In between arranging oxygen for dying relatives, recovering myself, and chasing a conference submission deadline, I tried to',
                A('visualize', href='https://avi-jit.github.io/covid-india/scatter#'),
                'the scale of the Indian crisis for Americans to better comprehend it. (Broken API)'
            )
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/667c51b662be4f33513ea6398bd1fd329032dab3d6c4e05cca7cc8e84d520d5e/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d3141374f6b462d587539654d4b6244367061365f30307a37725543333476797155', alt='Samsung', style='width:400px;')
            ),
            Td('Working with Samsung Research, I once voluntarily analyzed logged employee entry/exit data to analyze trends and share lessons with the Director of Samsung R&D Bengaluru. Turns out, attendance peaks around (free) lunchtime!')
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/ff92bad8bdef26a64ad6824017f1fd8ebac6d7751e4f85f99254028e0744a14e/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d315a5844736167526d77396e67685158384e7066345857545a3759424d44714545', alt='Campus', style='width:400px;')
            ),
            Td("As an undergrad, I deployed several campus-wide data analytics including a harmless rip-off of Zuckerberg's FaceMash which received 11,000 hits in 2 days, as well as hourly internet usage statistics via the Intranet portal.")
        ),
        Tr(
            Td(
                Img(src='https://camo.githubusercontent.com/96669ebc49721ef5d164b3965797859501b470fa3d7657c0b592895b866f4b86/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f6578706f72743d766965772669643d3145636c32333045374848694772647961423678322d2d764758536f6d484a4266', alt='Contraption', style='width:400px;')
            ),
            Td("I'm a big fan of mechanical contraptions (like the inventive devices that Tom builds to trap Jerry) so I made my own")
        )
    )
    )
    
    )