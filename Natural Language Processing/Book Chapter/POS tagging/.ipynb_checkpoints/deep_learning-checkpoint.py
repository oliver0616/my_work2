#Reference: https://techblog.cdiscount.com/part-speech-tagging-tutorial-keras-deep-learning-library/
#           https://github.com/Cdiscount/IT-Blog/blob/master/scripts/pos_tagging_neural_nets_keras.py
# using mutilayer feed-forward network https://www.otexts.org/fpp/9/3, https://en.wikipedia.org/wiki/Multilayer_perceptron
#==================================================================================================
#from __future__ import print_function
import random
import nltk
from nltk.corpus import treebank
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.layers import Dense, Dropout, Activation
from keras.models import Sequential
from keras.utils import np_utils, plot_model
from keras.wrappers.scikit_learn import KerasClassifier
import matplotlib.pyplot as plt

CUSTOM_SEED = 42

def add_basic_features(sentence_terms, index):
    """ Compute some very basic word features.
        :param sentence_terms: [w1, w2, ...]
        :type sentence_terms: list
        :param index: the index of the word
        :type index: int
        :return: dict containing features
        :rtype: dict
    """
    term = sentence_terms[index]
    return {
        'nb_terms': len(sentence_terms),
        'term': term,
        'is_first': index == 0,
        'is_last': index == len(sentence_terms) - 1,
        'is_capitalized': term[0].upper() == term[0],
        'is_all_caps': term.upper() == term,
        'is_all_lower': term.lower() == term,
        'prefix-1': term[0],
        'prefix-2': term[:2],
        'prefix-3': term[:3],
        'suffix-1': term[-1],
        'suffix-2': term[-2:],
        'suffix-3': term[-3:],
        'prev_word': '' if index == 0 else sentence_terms[index - 1],
        'next_word': '' if index == len(sentence_terms) - 1 else sentence_terms[index + 1]
    }

def untag(tagged_sentence):
    """
    Remove the tag for each tagged term.
    :param tagged_sentence: a POS tagged sentence
    :type tagged_sentence: list
    :return: a list of tags
    :rtype: list of strings
    """
    return [w for w, _ in tagged_sentence]

def transform_to_dataset(tagged_sentences):
    """
    Split tagged sentences to X and y datasets and append some basic features.
    :param tagged_sentences: a list of POS tagged sentences
    :param tagged_sentences: list of list of tuples (term_i, tag_i)
    :return:
    """
    X, y = [], []
    for pos_tags in tagged_sentences:
        for index, (term, class_) in enumerate(pos_tags):
            # Add basic NLP features for each sentence term
            X.append(add_basic_features(untag(pos_tags), index))
            y.append(class_)
    return X, y

def build_model(input_dim, hidden_neurons, output_dim):
    """
    Construct, compile and return a Keras model which will be used to fit/predict
    """
    model = Sequential([
        Dense(hidden_neurons, input_dim=input_dim),
        Activation('relu'),
        Dropout(0.2),
        Dense(hidden_neurons),
        Activation('relu'),
        Dropout(0.2),
        Dense(output_dim, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def plot_model_performance(train_loss, train_acc, train_val_loss, train_val_acc):
    """ Plot model loss and accuracy through epochs. """
    green = '#72C29B'
    orange = '#FFA577'
    fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 8))
    ax1.plot(range(1, len(train_loss) + 1), train_loss, green, linewidth=1,
             label='training')
    ax1.plot(range(1, len(train_val_loss) + 1), train_val_loss, orange,
            linewidth=1, label='validation')
    ax1.set_xlabel('# epoch')
    ax1.set_ylabel('loss')
    ax1.tick_params('y')
    ax1.legend(loc='upper right', shadow=False)
    ax1.set_title('Model loss through #epochs', fontweight='bold')
    ax2.plot(range(1, len(train_acc) + 1), train_acc, green, linewidth=1,
             label='training')
    ax2.plot(range(1, len(train_val_acc) + 1), train_val_acc, orange,
             linewidth=1, label='validation')
    ax2.set_xlabel('# epoch')
    ax2.set_ylabel('accuracy')
    ax2.tick_params('y')
    ax2.legend(loc='lower right', shadow=False)
    ax2.set_title('Model accuracy through #epochs', fontweight='bold')
    #with plt.xkcd():
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Ensure reproducibility
    np.random.seed(CUSTOM_SEED)
    sentences = treebank.tagged_sents(tagset='universal')[:100]
    print('a random sentence: \n-> {}'.format(random.choice(sentences)))
    tags = set([tag for sentence in treebank.tagged_sents() for _, tag in sentence])
    print('nb_tags: {}\ntags: {}'.format(len(tags), tags))

    # We use approximately 60% of the tagged sentences for training,
    # 20% as the validation set and 20% to evaluate our model.
    train_test_cutoff = int(.80 * len(sentences))
    training_sentences = sentences[:train_test_cutoff]
    testing_sentences = sentences[train_test_cutoff:]
    train_val_cutoff = int(.25 * len(training_sentences))
    validation_sentences = training_sentences[:train_val_cutoff]
    training_sentences = training_sentences[train_val_cutoff:]

    # For training, validation and testing sentences, we split the
    # attributes into X (input variables) and y (output variables).
    X_train, y_train = transform_to_dataset(training_sentences)
    X_test, y_test = transform_to_dataset(testing_sentences)
    X_val, y_val = transform_to_dataset(validation_sentences)
    # Fit our DictVectorizer with our set of features
    dict_vectorizer = DictVectorizer(sparse=False)
    dict_vectorizer.fit(X_train + X_test + X_val)
    # Convert dict features to vectors
    X_train = dict_vectorizer.transform(X_train)
    X_test = dict_vectorizer.transform(X_test)
    X_val = dict_vectorizer.transform(X_val)
    # Fit LabelEncoder with our list of classes
    label_encoder = LabelEncoder()
    label_encoder.fit(y_train + y_test + y_val)
    # Encode class values as integers
    y_train = label_encoder.transform(y_train)
    y_test = label_encoder.transform(y_test)
    y_val = label_encoder.transform(y_val)
    # Convert integers to dummy variables (one hot encoded)
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    y_val = np_utils.to_categorical(y_val)
    # Set model parameters
    model_params = {
        'build_fn': build_model,
        'input_dim': X_train.shape[1],
        'hidden_neurons': 512,
        'output_dim': y_train.shape[1],
        'epochs': 5,
        'batch_size': 256,
        'verbose': 1,
        'validation_data': (X_val, y_val),
        'shuffle': True
    }
    # Create a new sklearn classifier
    clf = KerasClassifier(**model_params)
    # Finally, fit our classifier
    hist = clf.fit(X_train, y_train)
    # Plot model performance
    plot_model_performance(
        train_loss=hist.history.get('loss', []),
        train_acc=hist.history.get('acc', []),
        train_val_loss=hist.history.get('val_loss', []),
        train_val_acc=hist.history.get('val_acc', [])
    )
    # Evaluate model accuracy
    score = clf.score(X_test, y_test, verbose=0)
    print('model accuracy: {}'.format(score))
    # Visualize model architecture
    plot_model(clf.model, to_file='model_structure.png', show_shapes=True)
    # Finally save model
    #clf.model.save('/tmp/keras_mlp.h5')