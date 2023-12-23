"""
Samvit Singhal
COMP 112-04 Introduction to Programming
2023-12-08


1. What were the 3 goals for your project?
    I wanted to use flow control, dictionaries, and file I/O.
2. Were the goals met?
    All goals, and more were met
3. How does this project illustrate your mastery of Python?
    I've used a library that was not taught in class, but is instrumental in the running of the program. Using lilypond
    has given me a unique understanding of how python can work with other languages.
4. What have you learned from doing this project?
    A big skill I've learned is how to convert a program from functions to a OOP based program. Doing this almost halved
    the number of lines, and made it much more readable. Furthermore, I have learned how to code music using lilypond.
    I have also developed the skill of thinking about possible errors and catching those.
"""

import subprocess
import inspect


def get_line_number():
    """find where an error is located"""
    frame = inspect.currentframe()
    return frame.f_lineno


if __name__ == '__main__':
    # Dr. Wolfe, please change the following filepath to where lilypond is located on your device
    lilypond_location = '/Users/sam/Documents/lilypond-2.24.2/bin/lilypond'
    f_lilypond = open('sheet_music.ly', 'w')  # open lilypond file (this is what I am generating code for)


    def is_valid_note(note_name):
        """find where an error is located"""
        return note_name in capital_lily.keys()


    class MusicGenerator:
        def __init__(self):
            """all the lists that are needed"""
            self.notes_flat = ['c\'', 'des\'', 'd\'', 'ees\'', 'e\'', 'f\'', 'ges\'',
                               'g\'', 'aes\'', 'a\'', 'bes\'', 'b\'']
            self.notes_sharp = ['c\'', 'cis\'', 'd\'', 'dis\'', 'e\'', 'f\'', 'fis\'',
                                'g\'', 'gis\'', 'a\'', 'ais\'', 'b\'']

            self.flat_keys = ['des', 'ees', 'f', 'ges', 'aes', 'bes', 'b']  # to refer
            self.sharp_keys = ['c', 'cis', 'd', 'dis', 'e', 'fis', 'g', 'gis', 'a', 'b', 'ais']  # to refer

            self.key2transpose_val_flat = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
            self.key2transpose_val_sharp = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']

            self.scale = '\n\n\\version "2.24.2"\n\\new Staff {\n\omit Staff.TimeSignature\n\omit Staff.BarLine'

        def major(self, key):
            """generate major scale"""
            if key in self.flat_keys:  # to generate in the right key
                notes = self.notes_flat
                key2transpose_val = self.key2transpose_val_flat
            elif key in self.sharp_keys:
                notes = self.notes_sharp
                key2transpose_val = self.key2transpose_val_sharp

            step_index = key2transpose_val.index(key)
            intervals = [2, 2, 1, 2, 2, 2, 1]  # formula to generate scale based on whole/half steps

            self.scale += '\n'
            scale_length = 0
            while scale_length <= 6:
                self.scale += notes[step_index]

                step_index += intervals[scale_length]
                step_index %= len(notes)
                scale_length += 1

            self.scale += '\n}'
            return self.scale

        def dorian(self, key):
            """generate dorian scale"""
            if key in self.flat_keys:  # to generate in the right key
                notes = self.notes_flat
                key2transpose_val = self.key2transpose_val_flat
            elif key in self.sharp_keys:
                notes = self.notes_sharp
                key2transpose_val = self.key2transpose_val_sharp

            step_index = key2transpose_val.index(key)
            intervals = [2, 1, 2, 2, 2, 1, 2]  # formula to generate scale based on whole/half steps

            self.scale += '\n'
            scale_length = 0
            while scale_length <= 6:
                self.scale += notes[step_index]

                step_index += intervals[scale_length]
                step_index %= len(notes)
                scale_length += 1

            self.scale += '\n}'
            return self.scale

        def lydian(self, key):
            """generate lydian scale"""
            if key in self.flat_keys:  # to generate in the right key
                notes = self.notes_flat
                key2transpose_val = self.key2transpose_val_flat
            elif key in self.sharp_keys:
                notes = self.notes_sharp
                key2transpose_val = self.key2transpose_val_sharp

            step_index = key2transpose_val.index(key)
            intervals = [2, 2, 2, 1, 2, 2, 1]  # formula to generate scale based on whole/half steps

            self.scale += '\n'
            scale_length = 0
            while scale_length <= 6:
                self.scale += notes[step_index]

                step_index += intervals[scale_length]
                step_index %= len(notes)
                scale_length += 1

            self.scale += '\n}'
            return self.scale

        def mixolydian(self, key):
            """generate mixolydian scale"""
            if key in self.flat_keys:  # to generate in the right key
                notes = self.notes_flat
                key2transpose_val = self.key2transpose_val_flat
            elif key in self.sharp_keys:
                notes = self.notes_sharp
                key2transpose_val = self.key2transpose_val_sharp

            step_index = key2transpose_val.index(key)
            intervals = [2, 2, 1, 2, 2, 1, 2]  # formula to generate scale based on whole/half steps

            self.scale += '\n'
            scale_length = 0
            while scale_length <= 6:
                self.scale += notes[step_index]

                step_index += intervals[scale_length]
                step_index %= len(notes)
                scale_length += 1

            self.scale += '\n}'
            return self.scale

        def diminished(self, key):
            """generate diminished scale"""
            if key in self.flat_keys:  # to generate in the right key
                notes = self.notes_flat
                key2transpose_val = self.key2transpose_val_flat
            elif key in self.sharp_keys:
                notes = self.notes_sharp
                key2transpose_val = self.key2transpose_val_sharp

            step_index = key2transpose_val.index(key)
            intervals = [2, 1, 2, 1, 2, 1, 2, 1]  # formula to generate scale based on whole/half steps

            self.scale += '\n'
            scale_length = 0
            while scale_length <= 7:
                self.scale += notes[step_index]

                step_index += intervals[scale_length]
                step_index %= len(notes)
                scale_length += 1

            self.scale += '\n}'
            return self.scale


    capital_lily = {  # dict for actual note names and lilypond note names
        'C': 'c', 'C#': 'cis', 'Db': 'des', 'D': 'd', 'D#': 'dis', 'Eb': 'ees', 'E': 'e', 'F': 'f', 'F#': 'fis',
        'Gb': 'ges', 'G': 'g', 'G#': 'gis', 'Ab': 'aes', 'A': 'a', 'A#': 'ais', 'Bb': 'bes', 'B': 'b'
        }
    symbol_list = ['∆#11', '∆', '-', '7', 'o']
    type_list = ['lydian', 'major', 'dorian', 'mixolydian', 'diminished']

    f_progression = open('chord_progression.txt', 'r')  # read chord_progression file

    line_number = 1
    for line in f_progression.readlines():
        try:
            # splitting note and symbol
            line_split = line.split()
            note_name = line_split[0]

            if not is_valid_note(note_name):  # invalid note error
                raise ValueError(f'Invalid note provided at line {line_number}')

            lilypond_note = capital_lily.get(note_name)  # basically an else block
            chord_found = False

            for symbol in symbol_list:
                if symbol in line:
                    chord_type = type_list[symbol_list.index(symbol)]  # retrieving chord type using symbol_list dict
                    method_to_call = getattr(MusicGenerator(), chord_type)  # figures out which scale generator to call
                    f_lilypond.write(method_to_call(lilypond_note))  # adds that code to lilypond file
                    chord_found = True
                    break

            if not chord_found:  # invalid chord type error
                raise ValueError(f'Invalid chord type provided at line {line_number}')

        except ValueError as e:  # printing error in console
            print(e)
        line_number += 1

    f_progression.close()
    f_lilypond.close()

    #  convert sheet_music.ly into a pdf (basically running the lilypond code)
    command = lilypond_location + ' sheet_music.ly'
    p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    retval = p.wait()
