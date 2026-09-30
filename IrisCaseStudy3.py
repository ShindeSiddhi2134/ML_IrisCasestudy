from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("iris Clasiffication case study")
    print("-"*30)
    dataset=load_iris()

    print("independent variable are:")
    print(dataset.feature_names)
    print("lenghth of independent variable are:",len(dataset.feature_names))

    print("dependent variable are:")
    print(dataset.target_names)
    print("length of dependent variable are:",len(dataset.target_names))
    
if __name__=="__main__":
    main()