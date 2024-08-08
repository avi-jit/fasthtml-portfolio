from fasthtml.fastapp import *
from fasthtml.common import *

def nav(sname:str, links:Dict[str, str]):
    return Nav(
        Ul(
            Li(
                Strong(sname)
            )
        ),
        Ul(
            *[Li(A(name, href=link)) for name, link in links.items()]
        )
    )
