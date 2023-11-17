
class Sequence:

    # constructor
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

    # getter and setter for id
    @property
    def id(self):
        return self._id 
    
    # the setter is here as an example
    """
    @id.setter
    def id(self, id):
        self._id = id
    """

    # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """

    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)

class DNASequence(Sequence):

    # these methods are only relevant for DNA sequences
    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    # translate method
    def translate_seq(self):
        # make codon table
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))

        # do translation
        # use a list comprehension and join to make a string
        aa_list = [codon_table[self.seq[start:start+3]] for start in range(0, len(self.seq) -2, 3)]
        protein = ''.join(aa_list)
        return protein
    
class ProteinSequence(Sequence):

    # descr is optional, default is an empty string
    def __init__(self, id, seq, descr=''):
        # call the constructor from the super class to set shared attributes
        super().__init__(id, seq)
        # aslo set the unique attribute
        self._descr = descr

    # getter for descr attribute
    @property
    def descr(self):
        return self._descr

    # method specific for protein sequences
    def get_prop_hydrophobic(self):
        count_hydrophobic = 0
        hydrophobic = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
        for hydro in hydrophobic:
            count = self.seq.count(hydro)
            count_hydrophobic += count
        return count_hydrophobic / len(self.seq)
    