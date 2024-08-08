from fasthtml.fastapp import *
from fasthtml.common import *

import fun
import build
import work

import constants
import utils

app, rt = fast_app(live=True)

@rt('/fun')
def get():
    return fun.fun()

@rt('/build')
def get():
    return build.build()

@rt('/work')
def get():
    return work.work()
    
@rt("/")
def get():
    name = constants.HEADING
    return Titled(
        utils.nav(constants.HEADING, constants.NAVDICT),
        #name, 
        P("I’m Avijit Thawani, a PhD from Univ of Southern California in langauge modeling."),
        Table(
        Tbody(
            Tr(
                Td(
                    A('Email', href='mailto:avijit.thawani@gmail.com', ),
                ),
                Td(
                    A('Resume', href='https://www.overleaf.com/read/pfvrgckrmmqv'),
                ),
                Td(
                    A('Instagram', href='https://instagram.com/avijit_thawani'),
                ),
                Td(
                    A('Twitter', href='https://twitter.com/thawani_avijit'),
                ),
                Td(
                    A('LinkedIn', href='https://www.linkedin.com/in/avi-jit/'),
                )
            )
        )
        ),
        affiliations()
    )
    
def affiliations():
    return Table(
    Tbody(
        Tr(
            Td('Affiliation'),
            Td('Mentors')
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/University_of_Southern_California_seal.svg/300px-University_of_Southern_California_seal.svg.png', alt='USC', style='width:200px;')
            ),
            Td(
                'My thesis committee:',
                A('Jay Pujara', href='http://jaypujara.org'),
                ',',
                A('Swabha Swayamdipta', href='http://swabhs.com'),
                ',',
                A('Dani Yogatama', href='https://dyogatama.github.io/'),
                '.'
            )
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Segoe_msr_logo.png/500px-Segoe_msr_logo.png', alt='MSR', style='width:200px;')
            ),
            Td(
                A('Microsoft Research Health Futures', href='https://www.microsoft.com/en-us/research/lab/microsoft-health-futures/'),
                ', Cambridge UK. Mentors: Stephanie Hyland, Flora Liu, Shruthi Bannur. Summer 2023.'
            )
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Amazon_Alexa_logo.svg/402px-Amazon_Alexa_logo.svg.png', alt='Alexa', style='width:200px;')
            ),
            Td(
                'Amazon Alexa Conversations Lab126 Sunnyvale. Mentors: Rohan Mukherjee, Hann Wang,',
                A('Arijit Biswas', href='https://www.amazon.science/author/arjit-biswas'),
                '. Summer 2022.'
            )
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Allen_Institute_for_Artificial_Intelligence.svg/500px-Allen_Institute_for_Artificial_Intelligence.svg.png', alt='AI2', style='width:200px;')
            ),
            Td(
                'Allen Institute of Artificial Intelligence (Aristo). Mentors:',
                A('Ashwin Kalyan', href='http://ashwinkalyan.com/'),
                ', Peter Clark. Summer 2021.'
            )
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Northeastern_seal.svg/300px-Northeastern_seal.svg.png', alt='NEU', style='width:200px;')
            ),
            Td(
                'Northeastern University, Boston. Mentor:',
                A('Byron Wallace', href='http://www.byronwallace.com/'),
                '. Summer 2018.'
            )
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Singapore_University_of_Technology_and_Design_logo.svg/500px-Singapore_University_of_Technology_and_Design_logo.svg.png', alt='SUTD', style='width:200px;')
            ),
            Td('Singapore University of Technology and Design, Singapore. Mentor: Yuen Chau. Summer 2016.')
        ),
        Tr(
            Td(
                Img(src='https://upload.wikimedia.org/wikipedia/en/4/4c/Official_Logo_of_IIT%28BHU%29%2CVaranasi%2CIndia%2C2013.png', alt='IIT BHU', style='width:200px;')
            ),
            Td(
                'I did my undergrad and masters in Computer Science at the Indian Institute of Technology',
                A('IIT BHU', href='https://www.iitbhu.ac.in/dept/cse'),
                'Varanasi.'
            )
        )
    )
)
serve()