from mycroft import MycroftSkill, intent_file_handler


class SayAWord(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('word.a.say.intent')
    def handle_word_a_say(self, message):
        randomword = ''

        self.speak_dialog('word.a.say', data={
            'randomword': randomword
        })


def create_skill():
    return SayAWord()

