import pandas as pd

def count_char(string, char):
    return string.count(char)

class FeatureEngine:
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        
        X_tmp = self.create_feature(X)
        return X_tmp
    
    def create_feature(self, X):
        X_tmp = X.reset_index(drop=True)
        
        X_tmp['url_length'] = X_tmp['url'].apply(len)
        X_tmp['n_dots'] = X_tmp['url'].apply(lambda x: count_char(x, '.'))
        X_tmp['n_hypens'] = X_tmp['url'].apply(lambda x: count_char(x, '-'))
        X_tmp['n_underline'] = X_tmp['url'].apply(lambda x: count_char(x, '_'))
        X_tmp['n_slash'] = X_tmp['url'].apply(lambda x: count_char(x, '/'))
        X_tmp['n_questionmark'] = X_tmp['url'].apply(lambda x: count_char(x, '?'))
        X_tmp['n_equal'] = X_tmp['url'].apply(lambda x: count_char(x, '='))
        X_tmp['n_at'] = X_tmp['url'].apply(lambda x: count_char(x, '@'))
        X_tmp['n_and'] = X_tmp['url'].apply(lambda x: count_char(x, '&'))
        X_tmp['n_exclamation'] = X_tmp['url'].apply(lambda x: count_char(x, '!'))
        X_tmp['n_space'] = X_tmp['url'].apply(lambda x: count_char(x, ' '))
        X_tmp['n_tilde'] = X_tmp['url'].apply(lambda x: count_char(x, '~'))
        X_tmp['n_comma'] = X_tmp['url'].apply(lambda x: count_char(x, ','))
        X_tmp['n_plus'] = X_tmp['url'].apply(lambda x: count_char(x, '+'))
        X_tmp['n_asterisk'] = X_tmp['url'].apply(lambda x: count_char(x, '*'))
        X_tmp['n_hastag'] = X_tmp['url'].apply(lambda x: count_char(x, '#'))
        X_tmp['n_dollar'] = X_tmp['url'].apply(lambda x: count_char(x, '$'))
        X_tmp['n_percent'] = X_tmp['url'].apply(lambda x: count_char(x, '%'))
        X_tmp['n_redirection'] = X_tmp['url'].str.count('//') - 1
           
        return X_tmp
    

class FeatureSelector:
    def __init__(self, features):
        self.features = features
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.features]