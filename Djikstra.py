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

