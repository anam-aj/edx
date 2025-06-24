        for arc in arcs:
            x, y = arc
            revised = self.revise(x, y)
            if revised:
                if len(self.domains[x]) == 0:
                    return False
                neighbors = self.crossword.neighbors(x)
                for neighbor in neighbors:
                    arc = (neighbor, x)
                    arcs.append(arc)

        #for variable in self.domains:
            #if len(self.domains[variable]) == 0:
                #return False

        return True

        else:
            for arc in arcs:
                x, y = arc
                revised = self.revise(x, y)
                if revised:
                    neighbors = self.crossword.neighbors(x)
                    for neighbor in neighbors:
                        arc = (x, neighbor)
                        arcs.append(arc)

                for variable in self.domains:
                    if len(self.domains[variable]) == 0:
                        return False

        return True


else:
            while arcs:
                arc = arcs.pop(0)
                x, y = arc
                revised = self.revise(x, y)
                if revised:
                    neighbors = self.crossword.neighbors(x)
                    for neighbor in neighbors:
                        arc = (x, neighbor)
                        arcs.append(arc)

                for variable in self.domains:
                    if len(self.domains[variable]) == 0:
                        return False
            return True
