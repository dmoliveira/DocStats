# coding: utf-8
import hashlib
from nltk.tokenize.api import StringTokenizer
from nltk.util import ngrams


class Document(object):

    def __init__(self, document_file_path, tokenizer=StringTokenizer, ngram=1):
        """
        Create a document objects with statistics about the given document.


        Keyword arguments:
        document_file_path -- Document absolute address
        tokenizer -- Tokenizer to break document text
                     (default NLTK Standard StringTokenizer)
        ngram -- Number of tokens that will be analyzed in pairs (default 1)
        """
        self.document_file_path = document_file_path
        self.id = hashlib.sha224(document_file_path).hexdigest()
        self.len = 0
        self.term_dict = {}
        self.max_freq = 0
        self.ngram = ngram
        self.tokenizer = tokenizer()

    def _consume_doc(self, document_file_path):
        """
        Read the document and extract terms statistics.


        Keyword arguments:
        document_file_path -- Document absolute address
        """
        document_tokenized = self.tokenizer.tokenize(open(document_file_path, 'r'))  # noqa
        self.len = len(document_tokenized)
        for token in ngrams(document_tokenized, self.ngram):
            self.term_dict[token] = self.term_dict.get(token, 0) + 1
            if self.max_freq < self.term_dict[token]:
                self.max_freq += self.term_dict[token]

    def get_freq(self, term, prob=False):
        """
        Returns term frequency.


        Keyword arguments:
        term -- Term to lookup at internal data.
        prob -- If the frequency will be returned raw
                or in probability (default False)
        """
        pass

    def get_terms(self, lower_threshold=0, upper_threshold=1, prob=False):
        """
        Return terms with frequency between the thresholds.


        Keyword arguments:
        lower_threshold -- Lower threshold frequency (default 0)
        upper_threshold -- Upper threshold frequency (default 1)
        prob -- If the threshold and frequency is to be 
                analyzed raw or in probability format (default False)
        """
        pass

    def has_term(self, term):
        """
        Returns if term exists in document.


        Keyword arguments:
        term -- Term to be checked at internal data.
        """
        return term in self.term_dict

    def save(self):
        """
        Effiently serialize document model to file.
        """
        pass

    def load(self):
        """
        Load effiently a serialized document model.
        """
        pass

    def get_max_freq_term(self):
        """
        Returns maximum frequency of a term in the document.
        """
        return self.max_freq

    def get_id(self):
        """
        Returns document id.
        """
        return self.id

    def get_len(self):
        """
        Returns total length of the document.
        """
        return self.len

    def get_vocab(self):
        """
        Returns document vocabulary.
        """
        return self.term_dict.keys()

    def get_vocab_len(self):
        """
        Returns document vocabulary length.
        """
        return len(self.get_vocab())

    def get_ngram(self):
        """
        Returns ngram size (i.e., the size of term pairs analyzed by token).
        """
        return self.ngram
