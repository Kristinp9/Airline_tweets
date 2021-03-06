
class CleanText(BaseEstimator, TransformerMixin):
    @staticmethod
    def _remove_mentions(input_text):
        return re.sub(r'@\w+', '', input_text)

    @staticmethod
    def _remove_urls(input_text):
        return re.sub(r'http.?://[^\s]+[\s]?', '', input_text)

    @staticmethod
    def _remove_stopwords(input_text):
        stopwords_list = stopwords.words('english')
        whitelist = [["n't", "not", "no"]]
        words = input_text.split() 
        clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1] 
        return " ".join(clean_words)

    @staticmethod
    def _remove_digits(input_text):
        return re.sub('\d+', '', input_text)

    @staticmethod
    def _to_lower(input_text):
        return input_text.lower()
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, **transform_params):
        clean_X = X.apply(self._remove_mentions).apply(self._remove_urls).apply(self._remove_stopwords).apply(self._remove_digits).apply(self._to_lower)
        return clean_X
