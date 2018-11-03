
# // Evaluation of a ranked list using a metric
# double Metric::scoreRanking(List<DataPoint>);

# // Select the value of a single named feature (index or name interpretation is fine).
# double DataPoint::getFeatureValue(FeatureID);

# // Select the entire feature vector (representing feature ids as array indices here)
# double [] DataPoint::getFeatureVector();

# // DataPoint
# {
# string id; // the document id
# string label; // the relevance score for this instance relative to the query this datapoint is in the list of, 
# // alternatively this could be a numeric value (0,1,2,3...).
# }

# // get the lists for each of the query ids as a separate list in an array.
# List<DataPoint>[] loadAll();



from random import randint
import numpy as np
def Ranking():
	# Assuming that loadAll returns the document lists for each of the query ids where queryID is represented by the index 
	queryList = loadAll()
	# we are given 
	for qNumber in queryList:
		# fvector gets the weights of the features that is used for the calculating the score/rank for the documents list 
		# for that particular qNumber (QueryNumber) if present, initially it returns an array of random numbers where the length of the array is the list features
		fvector = getFeatureVector(qNumber)

    # Setting the inital fvector to random values close to 0 for a start point
    for findex in len(fvector):
      fvector[findex] = randint(0,1)

		# The updatedListScore takes a document list and a fvector and computes the new score/rank for each of the documents in the passed list using the new feature weights, and returns the iupdated document list based on the feature vector. 
    qNumber = updatedListScore(fvector,qNumber)
		# Computes the evaluation score on the gold standard (Optimal Ranking)(g) and the new list (lscore) using the Evaluating 
		# Function, and returns a value that is the difference of (g-lscore).
		qscore  = scoreRanking(qNumber)

		for f in range(len(fvector)):
			# The coordinate decent keeps updating the coordinate till we cannot make any more improvements that is when,
			# you move to the next feature in the fvector
			while():
        #Getting the value of the feature at i and computing both left gradient and right gradient.
				valOfFeature	 = getFeatureValue(f)
				new_val_minus 	 = valOfFeature - 0.0001
				new_val_plus 	 = valOfFeature + 0.0001


				new_vectorminus = fvector[:]
				new_vectorminus[f] = new_val_minus
        qNumberleft = updatedListScore(new_vectorminus,qNumber)
				qscore_minus = scoreRanking(qNumberleft)


				new_vectorplus = fvector[:]
				new_vectorplus[f] = new_val_plus
				qNumberright = updatedListScore(new_vectorplus,qNumber)
				qscore_minus = scoreRanking(qNumberright)

				# Updating the value of the feature if appropriate 
				# Bigger score means you are far from the gold
        # If you are not making any more improvements move on to the next feature
				if(qscore <= qscore_plus and qscore <= qscore_minus ):
					break
				# Make movements in the direction which gives you greater Improvements 
				elif (qscore_minus < qscore_plus):
					fvector[f] = new_val_minus
          qNumber = qNumberleft

				else:
					fvector[f] = new_val_plus
          qNumber= qNumberright
  # At this point the program has the best weights we could find from the initial one.
  # we update the ranks in the qNumber
  qNumber = updatedListScore(fvector,qNumber)




def getDocumentVector(dID):
  # Assuming that we have an Map (dVector) that can be loaded given the docID it returns the document feature vector.
  return (dVector[dID])

#Function that takes in a list of datapoints and updates its label according to the new feature vector weight.
def updatedListScore(fvector,qNumber):
  for d in qNumber:
    docID = d.ID
    docID_VECTOR = getDocumentVector(d.ID)
    calculateLabel(docID_VECTOR, fvector,docID,qNumber)
  

# Takes in a a document vector and f vector and computes the dot product to find the new score and also updates ranking based on the score ?
def calculateLabel(docID_VECTOR, fvector,docID,qNumber):
  #Calculate Score
  score = np.dot(docID_VECTOR.T,fvector)
  #Update Score for the DocID
  updateScore(score,docID,qNumber)
  #Sort based on Score and update rank
  sortAndUpdate(qNumber)
  return (qNumber[docID])

def updateScore(score,docID,qNumber):
  # Updates the Score for the given docID in the qNumber(List of documents for the given Query)

def sortAndUpdate(qNumber)
  # sorts the list of documents in a qNumber(List of documents for the given Query) and updates their ranking accordingly
  # sort()
  # for docID, rank in qNumber.items():
  # def update():
    # d.label = new rank
