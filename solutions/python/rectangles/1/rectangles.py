def rectangles(strings):
    vertices_and_verticals = [(r, c) for  r, row in enumerate(strings) for c, character in enumerate(row) if any([character == '+', character == '|'])]
    vertices_and_horizontals = [(r, c) for  r, row in enumerate(strings) for c, character in enumerate(row) if any([character == '+', character == '-'])]
    vertices = [(r, c) for  r, row in enumerate(strings) for c, character in enumerate(row) if character == '+']

    rectangles = []
    edge = False

    def edge_check_horizontal(vertice_1, vertice_2):
            if vertice_2[1] - vertice_1[1] == 1:
                edge = True
            else:
                for k in range(vertice_1[1]+1, vertice_2[1]):
                    if (vertice_1[0], k) in vertices_and_horizontals and (vertice_2[0], k) in vertices_and_horizontals:
                        edge = True
                    else:
                        edge = False
                        break

            return edge

    for vertice_1 in vertices:
        for vertice_2 in vertices:
            if vertice_2[0] == vertice_1[0] and vertice_2[1] > vertice_1[1]: # look for a pair of vertices on same row
                edge = edge_check_horizontal(vertice_1, vertice_2)
                        
                if edge == False:
                    break
                else:
                    for vertice_3 in vertices: # look for paired horizontal vertices below
                        if vertice_3[0] > vertice_1[0]: # only look at subsequent rows
                            if vertice_3[1] == vertice_1[1]:
                                for vertice_4 in vertices:
                                    if vertice_4[0] == vertice_3[0] and vertice_4[1] == vertice_2[1]: # if vertices form rectangle
                                        # check for complete vertical edges
                                        for k in range(vertice_1[0]+1, vertice_3[0]):
                                            if (k, vertice_1[1]) in vertices_and_verticals and (k, vertice_2[1]) in vertices_and_verticals:
                                                edge = True
                                            else:
                                                edge = False
                                                break
                                        if edge == False:
                                            break

                                        edge = edge_check_horizontal(vertice_3, vertice_4)
                                        if edge == False:
                                            break
                                        else:   
                                            rectangles.append([vertice_1, vertice_2, vertice_3, vertice_4])
    
    rectangles_count = len(rectangles)
    return rectangles_count