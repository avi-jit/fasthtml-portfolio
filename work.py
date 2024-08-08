from fasthtml.fastapp import *
from fasthtml.common import *
import utils
import constants

PAPERS = Div(
    Ul(
        Li(
            Strong('Thawani A.'),
            ', Ghanekar S., Kumar D., Pujara J.',
            Em('Does Subword Vocabulary hold back Machine Translation?'),
            '. (submitted 2024).'
        ),
        Li(
            Strong('Thawani A.'),
            ', Ghanekar S., Zhu X., Pujara J.',
            Em('Learn Your Tokens: Word-Pooled Tokenization for Language Modeling'),
            '.',
            Strong('EMNLP 2023'),
            '|',
            A('Anthology', href='https://aclanthology.org/2023.findings-emnlp.662/'),
            '|',
            A('Arxiv', href='https://arxiv.org/abs/2310.11628'),
            '|',
            A('Poster', href='https://drive.google.com/file/d/1kBMsduKSNS28x1AjWJf1dz56ti5RYzMM/view?usp=sharing'),
            '|',
            A('Code', href='https://github.com/avi-jit/eTok')
        ),
        Li(
            Strong('Thawani A.'),
            ', Pujara J., Kalyan A.',
            Em('Estimating Numbers without Regression'),
            '. Negative Insights workshop at',
            Strong('EACL 2023'),
            '|',
            A('Arxiv', href='https://arxiv.org/abs/2310.06204'),
            '|',
            A('Presentation', href='https://underline.io/lecture/71866-estimating-numbers-without-regression')
        ),
        Li(
            'Kumar D*,',
            Strong('Thawani A*.'),
            Em('BPE with N-Grams and Skip-Grams'),
            '. Negative Insights workshop at',
            Strong('ACL 2022'),
            '|',
            A('Anthology', href='https://aclanthology.org/2022.insights-1.24/'),
            '|',
            A('Slides', href='https://docs.google.com/presentation/d/1TTNe6Obl0L69J2H-1i2JXaEhRsrmIDYCrlylT5wrROE/edit?usp=sharing'),
            '|',
            A('Reviews', href='https://openreview.net/forum?id=rHed93bCG-5'),
            '|',
            A('Code', href='https://github.com/pegasus-lynx/mwe-bpe')
        ),
        Li(
            Strong('Thawani A.'),
            ', et al.',
            Em('Numeracy enhances Literacy in Language Models'),
            '.',
            Strong('EMNLP'),
            '(2021).',
            A('Anthology', href='https://aclanthology.org/2021.emnlp-main.557/'),
            '|',
            A('Slides', href='https://drive.google.com/file/d/1-GIUOTRLavVzA_ynQ0HqTR_RMq2GezOI/view?usp=sharing'),
            '|',
            A('Video', href='https://drive.google.com/file/d/1QluCr79hAHkA_oCwD6JHUBQAQ81rMste/view?usp=sharing'),
            '|',
            A('Poster', href='https://drive.google.com/file/d/1DntS8pRlpsRnO3UpYZeo3wzAOJiHLfY1/view?usp=sharing'),
            '|',
            A('Thread', href='https://twitter.com/thawani_avijit/status/1434168008046301185'),
            '|',
            A('Code', href='https://github.com/avi-jit/numeracy-literacy'),
            '|',
            A('ACL21 Reviews', href='https://drive.google.com/file/d/1IUv9Rk3VqxceP58NyrEENAcr30P0etis/view?usp=sharing')
        ),
        Li(
            Strong('Thawani A.'),
            ', et al.',
            Em('Representing Numbers in NLP: a Survey and a Vision'),
            '.',
            Strong('NAACL'),
            '(2021).',
            A('Coverage', href='https://nlpnewsletter.substack.com/i/82970323/naacl'),
            '|',
            A('Anthology', href='https://www.aclweb.org/anthology/2021.naacl-main.53/'),
            '|',
            A('Arxiv', href='https://arxiv.org/abs/2103.13136'),
            '|',
            A('Slides', href='https://docs.google.com/presentation/d/1jDWLe6LiHtw5gK4klDQ9t5Ttt1llT38DlGgaybf4qnw/edit?usp=sharing'),
            '|',
            A('Video', href='https://drive.google.com/file/d/1muiAfVDx_Ul3Gqq9I-asn5p1AnLkrFTF/view?usp=sharing'),
            '|',
            A('Thread', href='https://twitter.com/thawani_avijit/status/1375033476194312194?s=20')
        ),
        Li(
            Strong('Thawani A.'),
            'et al.',
            Em('Entity Linking to Knowledge Graphs to Infer Column Types and Properties'),
            '.',
            Strong('SemTab @ ISWC'),
            '(2019).',
            A('PDF', href='http://www.cs.ox.ac.uk/isg/challenges/sem-tab/2019/papers/Tabularisi.pdf'),
            '|',
            A('Slides', href='http://www.cs.ox.ac.uk/isg/challenges/sem-tab/2019/slides/TabularISI.pdf')
        ),
        Li(
            Strong('Thawani A.'),
            'et al.',
            Em('Are Online Reviews of Physicians Biased Against Female Providers?'),
            Strong('MLHC'),
            '(2019).',
            A('PDF', href='https://www.mlforhc.org/s/Thawani.pdf'),
            '|',
            A('Code', href='https://github.com/avi-jit/RateMDs'),
        ),
        Li(
            Strong('Thawani, Avijit'),
            'et al.',
            Em('SWOW-8500: Word Association task for Intrinsic Evaluation of Word Embeddings'),
            '.',
            Strong('RepEval @ NAACL'),
            '(2019).',
            A('Anthology', href='https://www.aclweb.org/anthology/W19-2006'),
            '|',
            A('Poster', href='https://github.com/avi-jit/SWOW-eval/blob/master/1559781908296_small.pdf',),
            A('Code', href='https://github.com/avi-jit/SWOW-eval')
        ),
        Li(
            Strong('Thawani A.'),
            ', et al.',
            Em('SWOW-8500: Word Association task for Intrinsic Evaluation of Word Embeddings'),
            '.',
            Strong('RepEval @ NAACL'),
            '(2019).',
            A('Anthology', href='https://www.aclweb.org/anthology/W19-2006'),
            '|',
        ),
        Li(
            Strong('Thawani A.'),
            ', et al.',
            Em('SWOW-8500: Word Association task for Intrinsic Evaluation of Word Embeddings'),
            '.',
            Strong('RepEval @ NAACL'),
            '(2019).',
            A('Anthology', href='https://www.aclweb.org/anthology/W19-2006'),
            '|',
        ),
        Li(
            Strong('Thawani A.'),
            ', et al.',
            Em('SWOW-8500: Word Association task for Intrinsic Evaluation of Word Embeddings'),
            '.',
            Strong('RepEval @ NAACL'),
            '(2019).',
            A('Anthology', href='https://www.aclweb.org/anthology/W19-2006'),
            '|',
        ),
        Li(
            'Singh A.K.,',
            Strong('Thawani A.'),
            ', Gupta A., & Mundotiya R.K.',
            Em('Evaluating Opinion Summarization in Ranking'),
            '.',
            Strong('AIRS'),
            '(2017).',
            A('PDF', href='https://link.springer.com/content/pdf/10.1007%2F978-3-319-70145-5_17.pdf')
        ) 
    )
)

def work():
    name = constants.HEADING
    return Titled(
        utils.nav(constants.HEADING, constants.NAVDICT),
        #name, 
        "My research helps language models",
        Strong("tokenize"),
        "and represent text better.",
        'Other links to explore publications',
        Hr(), # other links
        Table(
        Tbody(
            Tr(
                Td(
                    A('Google Scholar', href='https://scholar.google.com/citations?user=i67YV2QAAAAJ')
                ),
                Td(
                    A('Semantic Scholar', href='https://www.semanticscholar.org/author/Avijit-Thawani/37574242')
                ),
                Td(
                    A('DBLP', href='https://dblp.uni-trier.de/pid/208/4386.html')
                ),
                Td(
                    A('ORCID', href='https://orcid.org/0000-0002-4289-3607')
                )
            )
        )
    ),
    #Hr(),
    "Here are my most recent and representative publications:",
    PAPERS,
    )
    
