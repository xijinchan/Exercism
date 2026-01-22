class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        if self.tonic in ['C','a','G','D','A','E','B','F#','e','b','f#','c#','g#','d#']:
            self.notes_all = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        else:
            self.notes_all = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]

    def chromatic(self):
        notes = [self.notes_all[(i + self.notes_all.index(self.tonic)) % 12] for i in range(len(self.notes_all))]
        return notes

    def interval(self, intervals):
        tonic_formatted = ''.join([k.upper() if i == 0 else k for i, k in enumerate(self.tonic)])
        intervals_index = ['m','M','A']
        intervals_nos = [intervals_index.index(k)+1 for k in intervals]
        intervals_nos_cumulative = [0] + [sum(intervals_nos[:k]) for k in range(1,len(intervals_nos)+1)]
        
        notes = [self.notes_all[(self.notes_all.index(tonic_formatted) + k) % 12] for k in intervals_nos_cumulative]
        return notes