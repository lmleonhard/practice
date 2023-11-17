class FastaFile:

    # constructor - only attribute is string containing a file name
    def __init__(self, file):
        self._file = file

    # getter for file name
    @property
    def file(self):
        return self._file
    
    # method to get DNASequence records out from a fasta file
    def get_seq_record(self, sequence_class):
        with open(self.file) as filehandle:
            for line in filehandle:
                if line.startswith('>'):
                    id = line.rstrip().lstrip('>')
                    seq = next(filehandle).rstrip()
                yield sequence_class(id, seq)    