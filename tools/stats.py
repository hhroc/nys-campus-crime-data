import json

def read_file(filename):

    with open(filename) as f:
        jsondata = json.loads(f.read())

    return jsondata

def show_stats(filename):

    print "Loading data ..."

    jsondata = read_file(filename)

    print "Processing data ..."

    max_2012_oncampus_forciblesexualoffense = 0
    max_index = -1
    index = 0
    for school in jsondata:
        if int(school['_2012_oncampus_forciblesexualoffense']) > max_2012_oncampus_forciblesexualoffense:
            max_2012_oncampus_forciblesexualoffense = int(school['_2012_oncampus_forciblesexualoffense'])
            max_index = index
        index += 1
            
    print "Done.\n\n"

    print "max_2012_oncampus_forciblesexualoffense: {0}".format(max_2012_oncampus_forciblesexualoffense)
    print "School: {0}".format(jsondata[max_index]['institution_name'])
    print "Woman: {0}".format(jsondata[max_index]['women_total'])
    print "Men: {0}".format(jsondata[max_index]['men_total'])

    print "\n\n"

if __name__ == '__main__':

    filename = '../data/Clery_Data_2014_NY_State.json.txt'
    show_stats(filename)
