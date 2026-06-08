from ultralytics.models import YOLO

if __name__ == "__main__":
    model = YOLO(
        r"C:\Users\Lenovo\Downloads\ultralytics-main\ultralytics-main\ultralytics\cfg\models\11\yolo11.yaml"
    ).load("yolo11n.pt")

    results = model.train(data="dataset/data.yaml", epochs=100, imgsz=640, batch=4)
