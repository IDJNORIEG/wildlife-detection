import cv2
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import threading
import time

# Diccionario de traducciones
TRANSLATIONS = {
    'es': {
        'title': 'Sistema de Detección de Fauna en Carreteras',
        'start': 'Iniciar Detección',
        'stop': 'Detener',
        'language': 'Idioma',
        'status': 'Estado:',
        'ready': 'Listo',
        'detecting': 'Detectando...',
        'stopped': 'Detenido',
        'alert': '¡ALERTA!',
        'animal_detected': 'Animal detectado en la vía',
        'distance': 'Distancia estimada',
        'speed': 'Velocidad recomendada',
        'reduce_speed': 'REDUZCA VELOCIDAD',
        'no_camera': 'No se pudo acceder a la cámara',
        'settings': 'Configuración',
        'sensitivity': 'Sensibilidad',
        'confidence': 'Confianza mínima'
    },
    'en': {
        'title': 'Wildlife Road Detection System',
        'start': 'Start Detection',
        'stop': 'Stop',
        'language': 'Language',
        'status': 'Status:',
        'ready': 'Ready',
        'detecting': 'Detecting...',
        'stopped': 'Stopped',
        'alert': 'ALERT!',
        'animal_detected': 'Animal detected on road',
        'distance': 'Estimated distance',
        'speed': 'Recommended speed',
        'reduce_speed': 'REDUCE SPEED',
        'no_camera': 'Could not access camera',
        'settings': 'Settings',
        'sensitivity': 'Sensitivity',
        'confidence': 'Minimum confidence'
    },
    'it': {
        'title': 'Sistema di Rilevamento Fauna Stradale',
        'start': 'Avvia Rilevamento',
        'stop': 'Ferma',
        'language': 'Lingua',
        'status': 'Stato:',
        'ready': 'Pronto',
        'detecting': 'Rilevamento...',
        'stopped': 'Fermato',
        'alert': 'ALLERTA!',
        'animal_detected': 'Animale rilevato sulla strada',
        'distance': 'Distanza stimata',
        'speed': 'Velocità consigliata',
        'reduce_speed': 'RIDURRE VELOCITÀ',
        'no_camera': 'Impossibile accedere alla fotocamera',
        'settings': 'Impostazioni',
        'sensitivity': 'Sensibilità',
        'confidence': 'Confidenza minima'
    },
    'fr': {
        'title': 'Système de Détection de Faune Routière',
        'start': 'Démarrer Détection',
        'stop': 'Arrêter',
        'language': 'Langue',
        'status': 'État:',
        'ready': 'Prêt',
        'detecting': 'Détection...',
        'stopped': 'Arrêté',
        'alert': 'ALERTE!',
        'animal_detected': 'Animal détecté sur la route',
        'distance': 'Distance estimée',
        'speed': 'Vitesse recommandée',
        'reduce_speed': 'RÉDUIRE VITESSE',
        'no_camera': 'Impossible d\'accéder à la caméra',
        'settings': 'Paramètres',
        'sensitivity': 'Sensibilité',
        'confidence': 'Confiance minimale'
    },
    'de': {
        'title': 'Wildtier-Erkennungssystem für Straßen',
        'start': 'Erkennung Starten',
        'stop': 'Stoppen',
        'language': 'Sprache',
        'status': 'Status:',
        'ready': 'Bereit',
        'detecting': 'Erkennung...',
        'stopped': 'Gestoppt',
        'alert': 'WARNUNG!',
        'animal_detected': 'Tier auf der Straße erkannt',
        'distance': 'Geschätzte Entfernung',
        'speed': 'Empfohlene Geschwindigkeit',
        'reduce_speed': 'GESCHWINDIGKEIT REDUZIEREN',
        'no_camera': 'Kein Zugriff auf Kamera',
        'settings': 'Einstellungen',
        'sensitivity': 'Empfindlichkeit',
        'confidence': 'Mindestvertrauen'
    },
    'ru': {
        'title': 'Система Обнаружения Диких Животных на Дороге',
        'start': 'Начать Обнаружение',
        'stop': 'Остановить',
        'language': 'Язык',
        'status': 'Статус:',
        'ready': 'Готов',
        'detecting': 'Обнаружение...',
        'stopped': 'Остановлено',
        'alert': 'ТРЕВОГА!',
        'animal_detected': 'Животное обнаружено на дороге',
        'distance': 'Расчетное расстояние',
        'speed': 'Рекомендуемая скорость',
        'reduce_speed': 'СНИЗИТЬ СКОРОСТЬ',
        'no_camera': 'Нет доступа к камере',
        'settings': 'Настройки',
        'sensitivity': 'Чувствительность',
        'confidence': 'Минимальная уверенность'
    }
}

class WildlifeDetectionApp:
    def __init__(self, root):
        self.root = root
        self.current_lang = 'es'
        self.root.title(TRANSLATIONS[self.current_lang]['title'])
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')
        
        self.cap = None
        self.is_detecting = False
        self.detection_thread = None
        
        # Variables de configuración
        self.sensitivity = tk.DoubleVar(value=0.5)
        self.min_confidence = tk.DoubleVar(value=0.6)
        
        # Cargar modelo YOLO pre-entrenado (simulación)
        self.load_model()
        
        # Crear interfaz
        self.create_ui()
        
    def load_model(self):
        """Simula la carga de un modelo de detección"""
        # En producción, aquí cargarías un modelo real como YOLOv8
        # import torch
        # self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        print("Modelo de detección cargado (simulación)")
        
    def create_ui(self):
        """Crea la interfaz de usuario"""
        # Frame superior con controles
        control_frame = tk.Frame(self.root, bg='#2d2d2d', padx=10, pady=10)
        control_frame.pack(fill=tk.X)
        
        # Selector de idioma
        lang_label = tk.Label(control_frame, 
                             text=TRANSLATIONS[self.current_lang]['language'],
                             bg='#2d2d2d', fg='white', font=('Arial', 10))
        lang_label.pack(side=tk.LEFT, padx=5)
        
        self.lang_combo = ttk.Combobox(control_frame, 
                                       values=['Español', 'English', 'Italiano', 
                                              'Français', 'Deutsch', 'Русский'],
                                       state='readonly', width=15)
        self.lang_combo.set('Español')
        self.lang_combo.bind('<<ComboboxSelected>>', self.change_language)
        self.lang_combo.pack(side=tk.LEFT, padx=5)
        
        # Botón iniciar/detener
        self.start_btn = tk.Button(control_frame, 
                                   text=TRANSLATIONS[self.current_lang]['start'],
                                   command=self.toggle_detection,
                                   bg='#4CAF50', fg='white',
                                   font=('Arial', 12, 'bold'),
                                   padx=20, pady=5)
        self.start_btn.pack(side=tk.LEFT, padx=20)
        
        # Estado
        self.status_label = tk.Label(control_frame,
                                     text=f"{TRANSLATIONS[self.current_lang]['status']} {TRANSLATIONS[self.current_lang]['ready']}",
                                     bg='#2d2d2d', fg='#4CAF50',
                                     font=('Arial', 10, 'bold'))
        self.status_label.pack(side=tk.LEFT, padx=20)
        
        # Frame de video
        self.video_frame = tk.Label(self.root, bg='black')
        self.video_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame de alertas
        alert_frame = tk.Frame(self.root, bg='#2d2d2d', padx=10, pady=10)
        alert_frame.pack(fill=tk.X)
        
        self.alert_label = tk.Label(alert_frame, text="", 
                                    bg='#2d2d2d', fg='white',
                                    font=('Arial', 14, 'bold'))
        self.alert_label.pack()
        
        # Frame de configuración
        config_frame = tk.LabelFrame(self.root, 
                                     text=TRANSLATIONS[self.current_lang]['settings'],
                                     bg='#2d2d2d', fg='white',
                                     font=('Arial', 10, 'bold'))
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Sensibilidad
        sens_label = tk.Label(config_frame, 
                             text=TRANSLATIONS[self.current_lang]['sensitivity'],
                             bg='#2d2d2d', fg='white')
        sens_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        
        sens_scale = tk.Scale(config_frame, from_=0.1, to=1.0, resolution=0.1,
                             orient=tk.HORIZONTAL, variable=self.sensitivity,
                             bg='#2d2d2d', fg='white', highlightthickness=0)
        sens_scale.grid(row=0, column=1, padx=10, pady=5)
        
        # Confianza mínima
        conf_label = tk.Label(config_frame, 
                             text=TRANSLATIONS[self.current_lang]['confidence'],
                             bg='#2d2d2d', fg='white')
        conf_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        
        conf_scale = tk.Scale(config_frame, from_=0.3, to=0.9, resolution=0.1,
                             orient=tk.HORIZONTAL, variable=self.min_confidence,
                             bg='#2d2d2d', fg='white', highlightthickness=0)
        conf_scale.grid(row=1, column=1, padx=10, pady=5)
        
    def change_language(self, event=None):
        """Cambia el idioma de la aplicación"""
        lang_map = {
            'Español': 'es',
            'English': 'en',
            'Italiano': 'it',
            'Français': 'fr',
            'Deutsch': 'de',
            'Русский': 'ru'
        }
        selected = self.lang_combo.get()
        self.current_lang = lang_map[selected]
        self.update_ui_text()
        
    def update_ui_text(self):
        """Actualiza los textos de la interfaz según el idioma"""
        self.root.title(TRANSLATIONS[self.current_lang]['title'])
        if self.is_detecting:
            self.start_btn.config(text=TRANSLATIONS[self.current_lang]['stop'])
            status_text = TRANSLATIONS[self.current_lang]['detecting']
        else:
            self.start_btn.config(text=TRANSLATIONS[self.current_lang]['start'])
            status_text = TRANSLATIONS[self.current_lang]['ready']
        self.status_label.config(text=f"{TRANSLATIONS[self.current_lang]['status']} {status_text}")
        
    def toggle_detection(self):
        """Inicia o detiene la detección"""
        if not self.is_detecting:
            self.start_detection()
        else:
            self.stop_detection()
            
    def start_detection(self):
        """Inicia la detección de animales"""
        self.cap = cv2.VideoCapture(0)  # Usa cámara 0 o cambia a video file
        
        if not self.cap.isOpened():
            messagebox.showerror("Error", 
                               TRANSLATIONS[self.current_lang]['no_camera'])
            return
            
        self.is_detecting = True
        self.start_btn.config(text=TRANSLATIONS[self.current_lang]['stop'],
                            bg='#f44336')
        self.status_label.config(
            text=f"{TRANSLATIONS[self.current_lang]['status']} {TRANSLATIONS[self.current_lang]['detecting']}",
            fg='#FFC107')
        
        self.detection_thread = threading.Thread(target=self.detection_loop)
        self.detection_thread.daemon = True
        self.detection_thread.start()
        
    def stop_detection(self):
        """Detiene la detección"""
        self.is_detecting = False
        if self.cap:
            self.cap.release()
        self.start_btn.config(text=TRANSLATIONS[self.current_lang]['start'],
                            bg='#4CAF50')
        self.status_label.config(
            text=f"{TRANSLATIONS[self.current_lang]['status']} {TRANSLATIONS[self.current_lang]['stopped']}",
            fg='#f44336')
        self.alert_label.config(text="")
        
    def detection_loop(self):
        """Loop principal de detección"""
        frame_count = 0
        
        while self.is_detecting:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            frame_count += 1
            
            # Redimensionar frame
            frame = cv2.resize(frame, (800, 600))
            
            # Simulación de detección (en producción usarías un modelo real)
            detections = self.simulate_detection(frame, frame_count)
            
            # Dibujar detecciones
            annotated_frame = self.draw_detections(frame, detections)
            
            # Mostrar alerta si hay detecciones
            if detections:
                self.show_alert(detections[0])
            else:
                self.root.after(0, self.alert_label.config, {'text': ''})
            
            # Convertir frame para Tkinter
            frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Actualizar imagen
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)
            
            time.sleep(0.03)  # ~30 FPS
            
    def simulate_detection(self, frame, frame_count):
        """Simula detección de animales (reemplazar con modelo real)"""
        detections = []
        
        # Simulación: detecta cada 50 frames con cierta probabilidad
        if frame_count % 50 == 0 and np.random.random() > (1 - self.sensitivity.get()):
            animals = ['deer', 'boar', 'fox', 'dog', 'cat', 'moose']
            animal = np.random.choice(animals)
            confidence = np.random.uniform(self.min_confidence.get(), 0.95)
            
            # Posición aleatoria en el frame
            h, w = frame.shape[:2]
            x1 = np.random.randint(0, w//2)
            y1 = np.random.randint(h//3, 2*h//3)
            x2 = x1 + np.random.randint(100, 200)
            y2 = y1 + np.random.randint(100, 200)
            
            detections.append({
                'animal': animal,
                'confidence': confidence,
                'bbox': (x1, y1, x2, y2),
                'distance': np.random.randint(10, 100)  # metros
            })
            
        return detections
        
    def draw_detections(self, frame, detections):
        """Dibuja las detecciones en el frame"""
        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            
            # Dibujar rectángulo
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
            
            # Texto
            label = f"{det['animal'].upper()} {det['confidence']:.2f}"
            cv2.putText(frame, label, (x1, y1-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            
            # Distancia
            dist_text = f"{det['distance']}m"
            cv2.putText(frame, dist_text, (x1, y2+25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            
        return frame
        
    def show_alert(self, detection):
        """Muestra alerta visual"""
        t = TRANSLATIONS[self.current_lang]
        alert_text = f"{t['alert']} {t['animal_detected']}\n"
        alert_text += f"{t['distance']}: {detection['distance']}m\n"
        alert_text += f"{t['reduce_speed']}"
        
        self.root.after(0, self.alert_label.config, 
                       {'text': alert_text, 'fg': '#ff0000'})
        
    def __del__(self):
        """Limpieza al cerrar"""
        if self.cap:
            self.cap.release()

def main():
    root = tk.Tk()
    app = WildlifeDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
