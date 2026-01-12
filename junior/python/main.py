from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    cantidad = 0
    if panel_height > roof_height or panel_width > roof_width:
        return cantidad
    cantx = roof_height // panel_height
    canty = roof_width // panel_width

    roof_base_h = cantx*panel_height
    roof_base_w = canty*panel_width

    cantidad = cantx*canty

    if roof_base_h == roof_height and roof_base_w == roof_width:
        return cantidad
    roof_down_h = roof_height - roof_base_h
    roof_down_w = roof_width

    roof_right_h = roof_base_h
    roof_right_w = roof_width - roof_base_w

    cantidad += calculate_panels(panel_height, panel_width, roof_right_w, roof_right_h)
    cantidad += calculate_panels(panel_height, panel_width, roof_down_w, roof_down_h)

    return cantidad
    


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
