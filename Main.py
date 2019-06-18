import os
import NoteToTxtConverter
import TxtToNoteConverter
import OverlapCleaner
from midicsv import CmConverter, McConverter

McConverter.convert()
OverlapCleaner.convert()
TxtToNoteConverter.convert()
NoteToTxtConverter.convert()
CmConverter.convert()
