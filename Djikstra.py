from itertools import permutations

class WeightedGraph:
    #initialization
    def _init_(self):
        self.cityList = {}

    def printGraph(self):
        #mengiterasi setiap city
        for city in self.cityList:
            #setiap kota print nama kota
            print(city, ":", self.cityList[city])

            # Print distances to neighboring cities
            for neighbor, distance in self.cityList[city].items():
                #print tetangga dan jarak
                print("    ->", neighbor, ":", distance, "KM")

    def tambahkanKota(self, kota):
        #jika kota tidak ada di cityList
        if kota not in self.cityList:
            #maka tambahkan kota
            self.cityList[kota] = {}
            return True
        return False

    def hapusKota(self, kotaDihapus):
        #jika kotaDihapus ada di cityList
        if kotaDihapus in self.cityList:
            # Remove the city from the city list
            del self.cityList[kotaDihapus]
            # Remove references to the deleted city from other cities
            for kota in self.cityList:
                #jika kotaDihapus ada di cityList[kota]
                if kotaDihapus in self.cityList[kota]:
                    #maka hapus kotaDihapus
                    del self.cityList[kota][kotaDihapus]
            return True
        return False

    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1][kota2] = jarak
            self.cityList[kota2][kota1] = jarak
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            if kota2 in self.cityList[kota1]:
                del self.cityList[kota1][kota2]
                del self.cityList[kota2][kota1]
                return True
        return False
    def dijkstra(self, source):
        # Initialize distances with infinity
        #distances = {city: float('inf') for city in self.cityList}
        
        distances = {}
        for city in self.cityList:
            distances[city] = float('inf')
        
        distances[source] = 0
        print (distances)
        # Initialize list of unvisited cities
        unvisited_cities = []
        for city in self.cityList:
            unvisited_cities.append(city)
        #unvisited_cities = list(self.cityList.keys())
        print (unvisited_cities)

        while unvisited_cities:
            # Find the unvisited city with the smallest distance
            min_distance = float('inf')
            closest_city = None
            #mengiterasi setiap kota yang belum dikunjungi
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari min_distance
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city

            # Remove the closest city from unvisited list
            unvisited_cities.remove(closest_city)

            # Update distances to neighboring cities
            for neighbor, weight in self.cityList[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil dari jarak kota tetangga
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
    
    def tsp(self):
        # Initialize variables
        shortest_distance = float('inf')
        shortest_path = []

        # Generate all permutations of cities
        cities = list(self.cityList.keys())
        for path in permutations(cities):
            # Calculate total distance for current permutation
            total_distance = 0
            for i in range(len(path) - 1):
                if path[i] in self.cityList and path[i + 1] in self.cityList[path[i]]:
                    total_distance += self.cityList[path[i]][path[i + 1]]
                else:
                    total_distance = float('inf')
                    break  # Break if path is invalid
            # Check if current permutation is shorter than the current shortest path
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path

        return shortest_path, shortest_distance

    # Example usage with Dijkstra's algorithm:
    petaArab = WeightedGraph()
    petaArab.tambahkanKota("Yanbu")
    petaArab.tambahkanKota("Madinah")
    petaArab.tambahkanKota("Kota Badar")
    petaArab.tambahkanKota("Al Henakiyah")
    petaArab.tambahkanKota("Rabigh")
    petaArab.tambahkanKota("Mahd adh Dhahab")
    petaArab.tambahkanKota("Jeddah")
    petaArab.tambahkanKota("Ta'if")
    petaArab.tambahkanKota("Turbah")
    petaArab.tambahkanKota("Ranyah")
    petaArab.tambahkanKota("Al Khurma")
    petaArab.tambahkanKota("Dariyah")
    petaArab.tambahkanKota("Ar Rass")
    petaArab.tambahkanKota("Al Quwaiiyah")
    petaArab.tambahkanKota("Layla")
    
    petaArab.tambahkanJalan("Yanbu","Madinah", 245)
    petaArab.tambahkanJalan("Yanbu","Kota Badar",100)
    petaArab.tambahkanJalan("Yanbu","Rabigh",195)
    petaArab.tambahkanJalan("Madinah","Kota Badar",152)
    petaArab.tambahkanJalan("Madinah","Al Henakiyah",121)
    petaArab.tambahkanJalan("Madinah","Mahd adh Dhahab",193)
    petaArab.tambahkanJalan("Kota Badar","Rabigh",123)
    petaArab.tambahkanJalan("Kota Badar","Ta'if",403)
    petaArab.tambahkanJalan("Al Henakiyah","Al Khurma",444)
    petaArab.tambahkanJalan("Al Henakiyah","Dariyah",729)
    petaArab.tambahkanJalan("Al Henakiyah","Ar Rass",355)
    petaArab.tambahkanJalan("Rabigh","Mahd adh Dhahab",272)
    petaArab.tambahkanJalan("Rabigh","Jeddah",156)
    petaArab.tambahkanJalan("Mahd adh Dhahab","Ta'if",302)
    petaArab.tambahkanJalan("Mahd adh Dhahab","Al Khurma",262)
    petaArab.tambahkanJalan("Mahd adh Dhahab","Dariyah",729)
    petaArab.tambahkanJalan("Jeddah","Ta'if",176)
    petaArab.tambahkanJalan("Jeddah","Mahd adh Dhahab",367)
    petaArab.tambahkanJalan("Ta'if","Turbah",159)
    petaArab.tambahkanJalan("Turbah","Al Khurma",100)
    petaArab.tambahkanJalan("Turbah","Ranyah",185)
    petaArab.tambahkanJalan("Ranyah","Al Khurma",143)
    petaArab.tambahkanJalan("Ranyah","Al Quwaiiyah",513)
    petaArab.tambahkanJalan("Ranyah","Layla",522)
    petaArab.tambahkanJalan("Al Khurma","Dariyah",643)
    petaArab.tambahkanJalan("Al Khurma","Al Quwaiiyah",470)
    petaArab.tambahkanJalan("Dariyah","Ar Rass",411)
    petaArab.tambahkanJalan("Dariyah","Al Quwaiiyah",174)
    petaArab.tambahkanJalan("Dariyah","Layla",310)
    petaArab.tambahkanJalan("Al Quwaiiyah","Ar Rass",328)
    petaArab.tambahkanJalan("Al Quwaiiyah","Layla",329)
    
    petaArab.printGraph()
    shortest_distances = petaArab.dijkstra("Madinah")
    print("Shortest distances from Madinah to other cities:")
    for city, distance in shortest_distances.items():
        print(city, ":", distance ,"KM")
    shortest_path, shortest_distance = petaArab.tsp()
    print("Shortest TSP path:", shortest_path)
    print("Shortest TSP distance:", shortest_distance)
