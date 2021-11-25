from jenkins_demo import fact

def jenkins_test():
    ans = fact(0)
    assert ans==1

    ans = fact(1)
    assert ans==1

    ans = fact(6)
    assert ans==720

if __name__ == '__main__':
    try: 
        jenkins_test()
    except AssertionError as e:
        print("Error in running tests")
        raise e
    
    print("Passed all tests!")

