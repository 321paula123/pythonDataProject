#-------------------------------------------------------------------------------
# Author:      Paula Young
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from scipy import stats
import pandas
import textwrap3

def main():
    # Each coding exercise (part 1, 2, and 3) is encapsulated in a function.
    # By running Young_Paula_Coding_Exercise, main() runs all three of these exercises.
    Exercise_1()
    Exercise_2()
    Exercise_3()

def Exercise_1():
    # The iris data will be read-in and transformed into a set of iris objects
    iris_set = set()

    # Error handling for fileIO
    try:
        input = open("Iris_Data.csv",'r')
        input.readline()  # Read the first line of column descriptions to skip past it.

        # Read each line of the Excel file. Split the line contents using ',' then remove whitespace.
        for line in input:
            iris_attributes_list = line.split(',')
            # Convert each token from a string to a float, and store it in a list.
            iris_attributes_float = []
            for attribute in iris_attributes_list:
                # Not all tokens can be converted to numbers.
                # Visual inspection shows that all irises have data, so if a token can't be converted to a float,
                # it is a space/new line/other... which is not important for our purposes.
                try:
                    # convert the attribute to a float
                    iris_attributes_float.append(float(attribute.strip()))
                except:
                    # if the token was not convertible to a number, we do not care about it for our purposes.
                    pass

                # The loop above builds a list of attributes for the line of iris data being accessed.
                # The first 5 attributes are all that we need.
                # We don't want to use the list to create an iris object before it is populated with all five attributes.
                if len(iris_attributes_float) == 5:
                    # Create a new iris object and add it to the set of irises.
                    new_iris = Iris(iris_attributes_float[0],iris_attributes_float[1],iris_attributes_float[2],iris_attributes_float[3],iris_attributes_float[4])
                    iris_set.add(new_iris)
                    # There is no need to continue reading for additional attributes - break to next line.
                    break
    except IOError as description:
        print("File IO Error Occurred", description)
    finally:
        # Close the file
        input.close()

    # Uncomment this code to verify that 150 lines of iris data was read in.
    # print(len(iris_set))

    # Initialize counters for each of the iris species.
    countSpecies0 = 0
    countSpecies1 = 0
    countSpecies2 = 0

    # Iterate over the set of irises, and increment the counters for each species.
    for iris in iris_set:
        if getattr(iris,"label") == 0:
            countSpecies0 += 1
        elif getattr(iris,"label") == 1:
            countSpecies1 += 1
        elif getattr(iris,"label") == 2:
                countSpecies2 += 1

    # Print the results.
    print("------------------------------------------------------------------------------------------------------------")
    print("\nPart 1: Regression Modeling")
    print()
    print("Part 1a - The number of Irises that belong to each species:")
    print("\tSpecies 0: "+ str(countSpecies0))
    print("\tSpecies 1: "+ str(countSpecies1))
    print("\tSpecies 2: "+ str (countSpecies2))

    #Initialize lists to store petal data, and sepal data (for use in regression)
    petal_list = []
    sepal_list = []

    # This will help with creating the scatter plot legend
    species_0_found = False
    species_1_found = False
    species_2_found = False

    # Create a Scatterplot
    for iris in iris_set:
        if getattr(iris, "label") == 0:
            if not species_0_found:
                plt.scatter(getattr(iris,"petal_length"), getattr(iris, "sepal_length"), color='r',label='Species 0' )
                species_0_found = True
            else:
                plt.scatter(getattr(iris, "petal_length"), getattr(iris, "sepal_length"), color='r')
        elif getattr(iris, "label") == 1:
            if not species_1_found:
                plt.scatter(getattr(iris, "petal_length"), getattr(iris, "sepal_length"), color='g',label='Species 1')
                species_1_found = True
            else:
                plt.scatter(getattr(iris, "petal_length"), getattr(iris, "sepal_length"), color='g')
        elif getattr(iris, "label") == 2:
            if not species_2_found:
                plt.scatter(getattr(iris, "petal_length"), getattr(iris, "sepal_length"), color='b',label='Species 2')
                species_2_found = True
            else:
                plt.scatter(getattr(iris, "petal_length"), getattr(iris, "sepal_length"), color='b')
        # While iterating through the irises, store their petal and sepal lengths in lists
        petal_list.append(getattr(iris,"petal_length"))
        sepal_list.append(getattr(iris,"sepal_length"))

    # Scatterplot labels
    plt.xlabel("Petal Length")
    plt.ylabel("Sepal Length")
    plt.title("Sepal vs. Petal Length for Irises")
    plt.legend()
    plt.show()

    print()
    print("Part 1b:")
    print("My observations about the scatter plot: ")
    print()

    # Print my observations about the scatter plot
    text_lines = textwrap3.wrap("Species 0 typically has the shortest petal and sepal lengths, while Species 2 tends to have the longest petal and sepal lengths. Species 1 has petal and sepal lengths inbetween those of Species 0 and 2. All sepal lengths are at least 4 units. There appears to be a roughly linear relationship between petal length and sepal length for Species 1 and 2. And generally speaking for all irises, sepal length tends to increase as petal length increases. Species 0 is the most easily distinguishable species on the basis of petal and sepal length. *Note that the scale increments for the y-axis (sepal length) are half of the petal length x-axis increments.",110)
    for line in text_lines:
        print(line)
    print()

    # Part 1c - Regression
    # Source: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.linregress.html
    slope, intercept, r_value, p_value, std_err = stats.linregress(petal_list, sepal_list)
    print("Part 1c:")
    print("\tThe linear regression equation is: ")
    print("\tSepal Length = "+str(round(slope,2))+"*(Petal Length) + "+str(round(intercept,2)))

    # Print my description of the regression results
    print()
    print("Description of Regression Results:")
    text_lines = textwrap3.wrap("For every unit that petal length increases, the linear regression equation predicts that iris sepal length will increase by 0.4 units. Sepal length starts at a higher initial value (4.3) according to the regression model, but sepal length does not increase in length as much, relative to petal length.",110)
    for line in text_lines:
        print(line)

# Definition of an Iris object
class Iris (object):
    # Constructor
    def __init__ (self,sepal_length, sepal_width, petal_length, petal_width, label):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.label = label

#---------------------------------Exercise 2 ---------------------------------------------------------------------------
def Exercise_2():
    # Define a function to calculate the Hamming distance between two strings.
    def distance(str1, str2):
        distance = 0
        # Define sets to identify lower and upper case letters, and their pairings.
        lowerUpperSet = [{'a', 'A'}, {'b', 'B'}, {'c', 'C'}, {'e', 'E'}, {'f', 'F'}, {'g', 'G'}, {'h', 'H'}, {'i', 'I'},
                         {'j', 'J'}, {'k', 'K'}, {'l', 'L'}, {'m', 'M'}, {'n', 'N'}, {'o', 'O'}, {'p', 'P'}, {'q', 'Q'},
                         {'r', 'R'}, {'s', 'S'}, {'t', 'T'}, {'u', 'U'}, {'v', 'V'}, {'w', 'W'}, {'x', 'X'},
                         {'y', 'Y'}, {'z', 'Z'}]

        lowercases = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        uppercases = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

        # If the strings are identical, the distance is 0
        if str1 == str2:
            return 0

        # Prevent Index Out of Bounds Errors
        if len(str1) == len(str2):
            # Compare letters of each string at the same indexes.
            for index in range(len(str1)):

                # If the letters don't match exactly, add 1 to distance.
                if str1[index] != str2[index]:
                    distance += 1

                    # If capitalization does not match, add 0.5
                    if (str1[index] in lowercases and str2[index] in uppercases) or (str1[index] in uppercases and str2[index] in lowercases):
                        distance += 0.5

                    # There are instances where the above two distance additions are inaccurate. The following corrects this.
                    for pair in lowerUpperSet:
                        # This identifies letters that are actually the same, just capitalized differently.
                        if str1[index] in pair and str2[index] in pair:

                            # First letter capitalization does not add distance. Subtract 1.5 to bring the distance
                            # down to zero (previously: 1 was added for the letters not matching, and 0.5 was added
                            # for the difference in capitalization)
                            if index == 0:
                                distance -= 1.5

                            # If it's not the first letter, and the letters are the same... just capitalized differently,
                            # subtract 1 so that the distance is only 0.5 (to account for the capitalization difference).
                            else:
                                distance -= 1

                    # The letters s and z (with matching capitalization) are considered the same, with distance 0.
                    # Distance for mismatched capitalization has already been accounted for above.
                    if str1[index] in {'s','S'} and str2[index] in {'z','Z'}:
                        # Subtract 1 to acknowledge that s and z are considered 0 distance apart, unless their capitalization differs.
                        distance -= 1

                    elif str1[index] in {'z','Z'} and str2[index] in {'s','S'}:
                        # Again, subtract 1 to acknowledge s and z as equivalent letters.
                        distance -= 1

            return distance
        else:
            print("These strings are different lengths and cannot be compared.")

    # To test the distance function, uncomment the following code:
    #print()
    #print(str(distance("Kitten", "kitten")) + "   0")
    #print(str(distance("kitten", "KiTten")) + "   0.5")
    #print(str(distance("Puppy", "POppy")) + "   1.5")
    #print(str(distance("make", "Mage")) + "   1")
    #print(str(distance("MaiSY", "MaiZy")) + "   0.5")
    #print(str(distance("Eagle", "Eager")) + "   2")
    #print(str(distance("Sentences work too", "Sentences wAke too"))+ "   3.5")
    #print(str(distance("analyze", "analyse")) + "   0")
    #print(str(distance("analyze", "analyZe")) + "   0.5")

    # Print Results
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("Part 2: Implementing an Edit-Distance Algorithm (a variation of Hamming Distance)")
    print('\tPart a: "data Science" to  "Data Sciency"')
    print("\tDistance: "+ str(distance("data Science", "Data Sciency")))
    print()
    print('\tPart b: "organizing" to "orGanising"')
    print("\tDistance: " + str(distance("organizing","orGanising")))
    print()
    print('\tPart c: "AGPRklafsdyweIllIIgEnXuTggzF" to "AgpRkliFZdiweIllIIgENXUTygSF"')
    print("\tDistance: "+ str(distance("AGPRklafsdyweIllIIgEnXuTggzF","AgpRkliFZdiweIllIIgENXUTygSF")))
    print()

    # Print my description of Hamming distance applications.
    #text_lines = textwrap3.wrap("The Hamming distance algorithm helps identify similar words. This distance is an indication of whether words are the same, have the same meaning (but different capitalization), or have the same root (or share some other similar structure). Getting the distance between words would be useful component of an algorithm comparing research articles, or any articles/documents. This would probably involve finding the frequent words of each document, and getting the distance between each possible pairing of frequent words from different documents. By identifying articles that are similar, it becomes easier to identify groupings and make recommendations. For example, you read this article that talks a lot about 'x', and another article also discusses 'x' and words closely related to 'x' frequently, therefore it might also be a good reference for you. The Hamming distance could also be a component of an algorithm that looks for plagiarism. And I would not be surprised if the Hamming distance or something similar is incorporated into Google searches.", 110)
    #for line in text_lines:
    #    print(line)

# Exercise 3 -----------------------------------------------------------------------------------------------------------
def Exercise_3():

    # Create a dataframe in Pandas to store the data.
    try:
        df = pandas.read_csv('patent_drawing.csv')
    except IOError:
        print("Error reading file")

    # Part a - Count how many of the rows have the words "view" or "perspective" but do not include "bottom", "top",
    # "front" or "rear" in  in the description.
    count_not_standard_perspective = 0

    # Define a dictionary to store patent ids and a corresponding count of the number of associated descriptions.
    descriptions_per_id = {}

    # Iterate through each of the rows of the csv file
    # df.shape[0] is the number of rows in the file
    for row in range(df.shape[0]):
        # This pulls the patent description, found in the third column.
        description = df.iloc[row][2]
        # Create a list of the words found in this description.
        description_words = description.split()
        is_Perspective = False
        # Check if the words in the description satisfy the criteria to be considered a non-standard perspective
        for word in description_words:
            if (word.strip() == "perspective" or word.strip() == "view"):
                is_Perspective = True
        # If the description is a perspective, the next step is to check for directional words.
        # This needs to go outside the above loop to prevent double counting (if a description includes both perspective and view).
        if is_Perspective:
            has_direction = False
            # Check if the description has directional words such as top/bottom/front/rear using a new loop
            for word2 in description_words:
                if (word2.strip() == "bottom" or word2.strip() == "top" or word2.strip() == "front" or word2.strip() == "rear"):
                    has_direction = True
            # If there is not a top/bottom/front/rear word, and there is either 'perspective' or 'view' , increment the counter.
            if not has_direction:
                count_not_standard_perspective += 1

        # Part 3b - the average number of drawing descriptions per patent.

        # Build the dictionary (keys: patent id's, values: number of descriptions corresponding to the patent)
        # Get the patent id
        id = df.iloc[row][1].strip()
        # Check if the patent id exists in the dictionary. If it does, increment the value (tracking the number of
        # descriptions per patent). If not, add the patent id to the dictionary.
        # Visual inspection of the file shows that there is a description for every line where an id is listed.
        if id in descriptions_per_id.keys():
            descriptions_per_id[id] = descriptions_per_id.get(id) + 1
        else:
            descriptions_per_id[id] = 1

    average_descriptions = 0
    total_ids = 0
    total_descriptions = 0
    # For each patent id in the dictionary:
    for key in descriptions_per_id.keys():
        # Increment the count of the number of patents
        total_ids += 1
        # Add 1 to the dictionary value of the patent - this value tracks the number of descriptions the patent has.
        total_descriptions += descriptions_per_id.get(key)
    # Prevent division by zero error.
    if total_ids != 0:
        # Calculate the average number of descriptions per patent (number of descriptions / number of unique patents)
        average_descriptions = float(total_descriptions) / total_ids

    # A simpler approach for calculating the average number of descriptions per patent:
    # Average = (Number of descriptions, given by: df.shape[0]) / (len(set to which each of the ids has been added))

    print()
    print("------------------------------------------------------------------------------------------------------------")
    print("Part 3: Data Cleaning")
    print("\tThe number of field descriptions with a non-standard perspective: "+ str(count_not_standard_perspective))
    print("\tThe average number of descriptions per patent is: " + str(round(average_descriptions,2)))
    print()
    print("-----------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------
# Run Main()
if __name__ == '__main__':
    main()
