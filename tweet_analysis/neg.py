import pickle
import os

class Neg():
	def __init__(self):

		open_file = os.path.join(
			os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
			'lexicon_generation',
			'sentic_score'
		)
		with open(open_file, 'rb') as f:
			self.my_list = pickle.load(f)

	def get_token_score(self,token):
		token_pos=token_neg=token_count=pos_score= neg_score=0
		for sentic_score in self.my_list:
			#print sentic_score
			sentic_word = sentic_score[2]
			if token == sentic_word[:-2]:
				# token_pos = max(token_pos,float(sentic_score[0]))
				token_pos += float(sentic_score[0])
				token_neg += float(sentic_score[1])
				token_count += 1
				if token_pos==0 and token_neg==0:
					token_count-=1
		# print token_pos,token_neg,token_count
		if token_count:
			pos_score = token_pos/token_count
			neg_score = token_neg/token_count
		# print pos_score,neg_score
		# print token_pos
		if pos_score>neg_score:
			return pos_score	
		else:
			return -1*neg_score
			

	def get_sentiments(self, tokens):
		list_negation_words = ['nor','useless','no','never','not','without','against',"n't","nt"]

		sentence_end = [".",",",";",":",".","and","&","or","but",'?']

		score = 0
		token_count = 0

		# End for the last sentence(if not given)
		tokens.append(["."])

		# Becomes True on detection of negative word and false on sentence end
		neg_word = False
		neg_score = 0
		for token in tokens:
			token_score = self.get_token_score(token[0])

			if token[0] in list_negation_words:
				neg_word = True
				neg_score = 0
				print "Aha!!"

			elif (token[0] in sentence_end):
				# negate if tweet is not a question
				if token[0] != '?' and neg_word:
					score += -1*(neg_score)
				else:
					score += neg_score
				neg_word = False
				neg_score = 0

			elif neg_word:
				neg_score += (token_score)
			else:
				score += (token_score)
			if token_score!=0.0 and token[0] not in list_negation_words:
				token_count+=1
			print token[0], token_score, score

		if score>0.1 or score<(-0.1):
			return score/token_count
		else:
			return 0.0
