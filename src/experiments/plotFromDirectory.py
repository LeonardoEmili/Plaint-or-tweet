import fire, os, json
import matplotlib.pyplot as plt

'''
plots roc curves reading all the data from a directory
'''
<<<<<<< HEAD
def main(root='experiments', filterNames={'Multinomial_TFIDF', 'Multinomial', 'Bernoulli', 'EmbeddingsGaussian', 'EmbeddingsMultinomial', 'EmbeddingDiscretized'}):
=======
# 'TwitterBernoulliBOW(1,3)13', 'TwitterMultinomialBOW(1,3)13'
# 'TwitterBernoulliBOW(1,3)13', 'TwitterMultinomialBOW(1,3)13', 'TwitterMultinomialTfidfBOW(1,3)13'
# 'TwitterCategoricalFastText(1,3)13', 'TwitterGaussianFastText(1,3)13', 'TwitterMultinomialFastText(1,3)13'
# 'TwitterImdbBernoulliBOW(1,3)13', 'ImdbTwitterBernoulliBOW(1,3)13'
def main(root='experiments', filterNames={'RedditCategoricalFastText(1,3)105', 'RedditGaussianFastText(1,3)105', 'RedditMultinomialFastText(1,3)105'}):
>>>>>>> 52c0a3205c01ef6e1749eb744f788229897873e9
    curves = []
    files = os.listdir(root)
    for f in files:
        path = root+'/'+f
        if os.path.isfile(path):
            fp = open(path)
            d = json.load(fp)
            fp.close()
            if filterNames is None or d['name'] in filterNames:
                curves.append((d['name'], d['tpr'], d['fpr']))

    for c in curves:
        plt.plot(c[2], c[1], label=c[0])
    plt.legend()
    plt.show()

if __name__ == '__main__':
    fire.Fire(main)