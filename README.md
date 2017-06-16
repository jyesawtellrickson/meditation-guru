# Meditation Bot
A Meditation Bot built for Windows in Python. The 'Guru' will lead you through different lessons in meditation. Lessons are fully customisable and easy to add to in the meditation format.

## Lessons
Each meditation session is based around a lesson. A lesson consists of a txt file located in the 'lessons' folder. Lessons are made up of lines. Each line contains a string to be read to the student which is optionally prefixed with a integer which represents the length of the pause to follow the line. Note that within a line a pause can be created by using a comma (',').

## Training
To use the Bodhivista, he must be first initialised by creating a class, e.g.

Bodhivista = Guru()

One can then select a lesson with:

Bodhivista.choose_teaching()

And finally, a lesson can be begun with:

Bodhivista.teach()

The lesson will then run until completion.