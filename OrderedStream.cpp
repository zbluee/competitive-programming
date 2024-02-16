class OrderedStream {
public:
    std::vector<std::string> stream;
    int size;
    int ptr;
    OrderedStream(int n) : stream(n+1, ""),size(n+1), ptr(1){}
    
    vector<string> insert(int idKey, string value) {
        stream[idKey] = value;
        std::vector<std::string> result;

        if (idKey == ptr){
            while (ptr < size && stream.at(ptr) != ""){
                result.push_back(stream.at(ptr));
                ptr ++;
            }
        }
        return result;
    }
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */
