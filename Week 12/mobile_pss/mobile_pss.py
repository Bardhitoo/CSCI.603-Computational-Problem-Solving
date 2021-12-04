from Ball import Ball
from Rod import Rod

def test():
    root = Rod("Rod_A", 100,
               50,
               Rod("Rod_B", 100,
                   60,
                   Ball("Ball_A", 65, 30, 24),
                   40,
                   Rod("Roc_C", 150,
                       250,
                       Ball("Ball_B", 100, 50, 16),
                       200,
                       Ball("Ball_C", 100, 35, 20))
                   ),
               60,
               Ball("Ball_D", 40, 40, 50)
               )
    print(root.get_weight())
    print(root.width())
    a = 1

if __name__ == "__main__":
    test()
