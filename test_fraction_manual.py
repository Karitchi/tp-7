from fraction import Fraction


def test_fraction_initialization():
    print("=== Test de l'initialisation de la classe Fraction ===")

    # Test 1: Fraction valide
    try:
        f = Fraction(4, 8)
        print(
            f"Test 1 réussi : {f} (numérateur : {f.numerator}, dénominateur : {f.denominator})"
        )
    except Exception as e:
        print(f"Test 1 échoué : {e}")

    # Test 2: Denominator = 0 (précondition violée)
    try:
        f = Fraction(1, 0)
        print(
            "Test 2 échoué : Aucun problème détecté alors que le dénominateur est zéro."
        )
    except ValueError as e:
        print(f"Test 2 réussi : {e}")

    # Test 3: Numérateur ou dénominateur non entier (précondition violée)
    try:
        f = Fraction(1.5, 2)
        print(
            "Test 3 échoué : Aucun problème détecté alors que le numérateur n'est pas un entier."
        )
    except TypeError as e:
        print(f"Test 3 réussi : {e}")

    # Test 4: Fraction négative (vérification des signes)
    try:
        f = Fraction(-3, -9)
        print(
            f"Test 4 réussi : {f} (numérateur : {f.numerator}, dénominateur : {f.denominator})"
        )
    except Exception as e:
        print(f"Test 4 échoué : {e}")

    # Test 5: Fraction déjà irréductible
    try:
        f = Fraction(3, 7)
        print(
            f"Test 5 réussi : {f} (numérateur : {f.numerator}, dénominateur : {f.denominator})"
        )
    except Exception as e:
        print(f"Test 5 échoué : {e}")


def test_fraction_textual_representations():
    print("=== Test de la représentation textuelle des fractions ===")

    # Test 1: Fraction réduite avec un dénominateur différent de 1
    try:
        f = Fraction(3, 4)
        assert str(f) == "3/4", f"Échec Test 1 : attendu '3/4', obtenu {str(f)}"
        print("Test 1 réussi : Représentation correcte de 3/4")
    except AssertionError as e:
        print(e)

    # Test 2: Fraction réduite avec un dénominateur égal à 1
    try:
        f = Fraction(5, 1)
        assert str(f) == "5", f"Échec Test 2 : attendu '5', obtenu {str(f)}"
        print("Test 2 réussi : Représentation correcte de 5")
    except AssertionError as e:
        print(e)

    # Test 3: Fraction négative
    try:
        f = Fraction(-7, 3)
        assert str(f) == "-7/3", f"Échec Test 3 : attendu '-7/3', obtenu {str(f)}"
        print("Test 3 réussi : Représentation correcte de -7/3")
    except AssertionError as e:
        print(e)

    # Test 4: Fraction en nombre mixte (entier et fraction)
    try:
        f = Fraction(7, 3)
        assert (
            f.as_mixed_number() == "2 1/3"
        ), f"Échec Test 4 : attendu '2 1/3', obtenu {f.as_mixed_number()}"
        print("Test 4 réussi : Nombre mixte correct 2 1/3")
    except AssertionError as e:
        print(e)

    # Test 5: Fraction en nombre mixte négatif
    try:
        f = Fraction(-7, 3)
        assert (
            f.as_mixed_number() == "-2 1/3"
        ), f"Échec Test 5 : attendu '-2 1/3', obtenu {f.as_mixed_number()}"
        print("Test 5 réussi : Nombre mixte négatif correct -2 1/3")
    except AssertionError as e:
        print(e)

    # Test 6: Fraction réduite en entier comme nombre mixte
    try:
        f = Fraction(6, 3)
        assert (
            f.as_mixed_number() == "2"
        ), f"Échec Test 6 : attendu '2', obtenu {f.as_mixed_number()}"
        print("Test 6 réussi : Nombre entier correct en nombre mixte")
    except AssertionError as e:
        print(e)

    # Test 7: Fraction propre (valeur absolue < 1) comme nombre mixte
    try:
        f = Fraction(1, 4)
        assert (
            f.as_mixed_number() == "1/4"
        ), f"Échec Test 7 : attendu '1/4', obtenu {f.as_mixed_number()}"
        print("Test 7 réussi : Fraction propre correcte 1/4")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    test_fraction_initialization()
    test_fraction_textual_representations()
