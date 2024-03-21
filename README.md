## Flask Application Design for a German Language Learning Website

### HTML Files

- **index.html**: The homepage of the website, displaying a brief introduction to the website, available German lessons, and navigation to different sections.
- **lessons.html**: A page listing all available German lessons, with a brief description of each and a link to the corresponding lesson page.
- **lesson1.html**: The first lesson page, containing interactive exercises, grammar explanations, and vocabulary.
- **lesson2.html**: The second lesson page, with similar content to lesson1.html but focusing on different aspects of German grammar and vocabulary.
- **resources.html**: A page providing additional resources for German learners, such as online dictionaries, grammar guides, and pronunciation guides.

### Routes

- **/:** Displays the homepage (index.html).
- **lessons**: Displays the list of German lessons (lessons.html).
- **lesson/&lt;lesson_id&gt;**: Displays the corresponding lesson page, where "&lt;lesson_id&gt;" is a placeholder for the specific lesson number (e.g., lesson1.html).
- **resources**: Displays the resources page (resources.html).