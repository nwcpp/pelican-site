September/October 2010 Meeting
------------------------------

September 15: The Many Faces of D - Walter Bright
-------------------------------------------------

There are many mainstream programming paradigms -
imperative, object oriented, meta, functional, etc.
Each has their proponents and languages oriented around it.
But larger applications tend to not fit easily into any particular paradigm.

In extreme cases, developers will resort to using multiple languages
with an uneasy interface between them.
The `D programming language <http://www.digitalmars.com/d/index.html>`_
takes a different approach, offering multiple programming paradigms within one language,
making it easy to select the most suitable paradigm for each task within the application.

`Walter Bright <http://www.walterbright.com/>`_ graduated from Caltech in 1979
with a degree in mechanical engineering.
He worked for Boeing for 3 years on the development of the 757 stabilizer trim system.
He then switched to writing software, in particular compilers,
and has been writing them ever since.

There will be door prizes--3 copies of Andrei Alexandrescu's book,
`The D Programming Language
<http://www.amazon.com/D-Programming-Language-Andrei-Alexandrescu/dp/0321635361/>`_--plus
light refreshments.

**Update**: Here are `Walter's slides <http://www.nwcpp.org/images/stories/nwcpp-2010-09.pdf>`_.


October 20: Steve Yegge - Scaling and Standardizing Programming Language Analysis at Google
--------------------------------------------------------------------------------------------

Wednesday, October 20, 2010, at 7pm. 41/1511, Microsoft.
Come early to socialize and eat pizza.

**Abstract**: Modern IDEs and compilers generate a wealth of information,
and you can't have any of it.
Tools in the compiler family -- even the best IDEs -- tend to be monolithic, language-specific,
generally non-scalable special-purpose applications.
Even when they do support headless analysis, none of them do it the same way,
and very few of them can do cross-language analysis.
At Google, I've put together a team with the long-term goal of addressing these problems
in a general way.
We've built infrastructure to run IDE-quality code analyzers such
as `Eclipse <http://www.eclipse.org/>`_ and `clang <http://en.wikipedia.org/wiki/Clang>`_
over Google's entire corpus and all open-source code.
We translate the intermediate representations into a language-neutral index,
then serve the index data back through language-neutral APIs and query interfaces.
In this talk I'll share what we've done so far,
then about our longer-term plans for an open platform.

**Bio**: `Steve Yegge <http://steve-yegge.blogspot.com/>`_ graduated
from the University of Washington with a B.S. in Computer Science.
He spent five years as a developer and team lead at Geoworks,
several years at various startups,
and then more than six years at Amazon.com as a Senior Development Manager.
He joined Google in 2005 and is a Staff Software Engineer in the Kirkland office,
currently working on scaling language analysis.
Steve lives in downtown Kirkland with his lovely wife Linh and their faithful furry sidekick Cino.

**Update**: `Video <http://vimeo.com/16069687>`_ of Steve's talk.

Last Updated on Monday, 02 May 2011 12:17  
