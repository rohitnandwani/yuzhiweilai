
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def getParagraphSentiment(text):

            sentence_list = tokenize.sent_tokenize(text)
            paragraphSentiments=0.0

            number_of_sentences = 0

            sentiment_tag = 'Neutral'

            cumulativeVaderCompound = 0
            cumulativeNegativeVaderCompound = 0
            cumulativePositiveVaderCompound = 0
            negativity = 0


            for sentence in sentence_list:
                vaderSentiment = analyzer.polarity_scores(sentence)
                sentimentVaderCompound = vaderSentiment["compound"]
                #print "sentence"
                #print sentence
                #print "sentimentVaderCompound"
                #print sentimentVaderCompound
                #print("{:-<69} {}".format(sentence, str(vs["compound"])))
                if abs(sentimentVaderCompound) >= 0.25:
                    cumulativeVaderCompound = cumulativeVaderCompound + sentimentVaderCompound
                if sentimentVaderCompound <= -0.25:
                    cumulativeNegativeVaderCompound = cumulativeNegativeVaderCompound + abs(sentimentVaderCompound)
                if sentimentVaderCompound >= 0.25:
                    cumulativePositiveVaderCompound = cumulativePositiveVaderCompound + abs(sentimentVaderCompound)
                number_of_sentences = number_of_sentences + 1
                print number_of_sentences

                #paragraphSentiments += vs["compound"]
            #print("AVERAGE SENTIMENT FOR PARAGRAPH: \t" + str(round(paragraphSentiments/len(sentence_list), 4)))
            sentimentVaderCompoundAverage = cumulativeVaderCompound / float(number_of_sentences)

            try:
                negativity =  (cumulativeNegativeVaderCompound / float(cumulativePositiveVaderCompound + cumulativeNegativeVaderCompound))
            except:
                pass

            #print "sentimentVaderCompound"
            #print sentimentVaderCompound
            #print "cumulativeVaderCompound"
            #print cumulativeVaderCompound
            #print "cumulativePositiveVaderCompound"
            #print cumulativePositiveVaderCompound
            #print "cumulativeNegativeVaderCompound"
            #print cumulativeNegativeVaderCompound

            #Temporary fix until we start using sentiment tags in the model
            if negativity >= 0.42:
                sentimentVaderCompoundAverage = -0.33

            if sentimentVaderCompoundAverage <= -0.10 or negativity >= 0.42:#Because 42 is the answer to Life, Universe and Everything.
                sentiment_tag = 'Negative'
            elif sentimentVaderCompoundAverage >= 0.10:
                sentiment_tag = 'Positive'
            else:
                sentiment_tag = 'Neutral'
        except Exception as err:
            print err
            return err

        return jsonify({"success" : True, "sentiment" : sentimentVaderCompoundAverage, "sentimentTag" : sentiment_tag})


