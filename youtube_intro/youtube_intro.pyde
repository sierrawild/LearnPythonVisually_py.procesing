# YouTube Channel Intro - Particle Burst
# Cool animated effect that builds and explodes

particles = []
frame_count = 0
phase = 0  # 0=gather, 1=hold, 2=explode

recording = False
frames_saved = 0

def setup():
    size(1080, 1920)  # YouTube standard HD
    colorMode(HSB, 360, 100, 100, 100)
    
    # Create particles in a grid
    spacing = 40
    for x in range(0, width + spacing, spacing):
        for y in range(0, height + spacing, spacing):
            particles.append({
                'home_x': x,
                'home_y': y,
                'x': x,
                'y': y,
                'vx': 0,
                'vy': 0,
                'hue': random(180, 280),  # Blues to purples
                'size': random(3, 8),
                'speed': random(0.8, 1.2)
            })

def draw():
    global frame_count, phase, recording, frames_saved
    
    # Dark fade trail effect
    fill(0, 0, 0, 30)
    rect(0, 0, width, height)
    
    # Update phase
    if frame_count < 120:
        phase = 0  # Gathering
    elif frame_count < 180:
        phase = 1  # Holding at center
    elif frame_count < 300:
        phase = 2  # Exploding
    else:
        phase = 3  # Floating away
    
    # Center point
    cx = width / 2
    cy = height / 2
    
    # Update and draw particles
    for p in particles:
        if phase == 0:  # Pull toward center
            dx = cx - p['x']
            dy = cy - p['y']
            p['vx'] += dx * 0.0015 * p['speed']
            p['vy'] += dy * 0.0015 * p['speed']
            p['vx'] *= 0.95
            p['vy'] *= 0.95
            
        elif phase == 1:  # Hold and swirl
            angle = atan2(p['y'] - cy, p['x'] - cx)
            swirl = 0.03
            p['vx'] += cos(angle + swirl) * 0.5 - cos(angle) * 0.5
            p['vy'] += sin(angle + swirl) * 0.5 - sin(angle) * 0.5
            # Pull slightly inward
            p['vx'] -= (p['x'] - cx) * 0.001
            p['vy'] -= (p['y'] - cy) * 0.001
            p['vx'] *= 0.9
            p['vy'] *= 0.9
            
        elif phase == 2:  # Explode outward
            if frame_count == 180:  # Initial burst
                angle = atan2(p['home_y'] - cy, p['home_x'] - cx)
                force = random(8, 15) * p['speed']
                p['vx'] = cos(angle) * force
                p['vy'] = sin(angle) * force
            p['vx'] *= 0.97
            p['vy'] *= 0.97
            
        else:  # Float back home
            dx = p['home_x'] - p['x']
            dy = p['home_y'] - p['y']
            p['vx'] += dx * 0.002
            p['vy'] += dy * 0.002
            p['vx'] *= 0.95
            p['vy'] *= 0.95
        
        # Apply velocity
        p['x'] += p['vx']
        p['y'] += p['vy']
        
        # Draw particle
        noStroke()
        
        # Glow effect
        for i in range(3, 0, -1):
            alpha = 15 * (4 - i)
            fill(p['hue'], 80, 100, alpha)
            ellipse(p['x'], p['y'], p['size'] * i, p['size'] * i)
        
        # Core
        fill(p['hue'], 70, 100, 90)
        ellipse(p['x'], p['y'], p['size'], p['size'])
    
    # Center flash during explosion
    if phase == 2:
        flash = map(frame_count, 180, 210, 100, 0)
        if flash > 0:
            fill(0, 0, 100, flash)
            ellipse(cx, cy, 300, 300)
    
    # Text overlay (add your channel name here!)
    if phase == 1 or (phase == 2 and frame_count < 240):
        fill(0, 0, 100, 90)
        textAlign(CENTER, CENTER)
        textSize(120)
        text("Hello World!", cx, cy)
    
    frame_count += 1
    
    # Loop after 420 frames (~14 seconds at 30fps)
    if frame_count > 420:
        frame_count = 0
        # Respawn particles at home
        for p in particles:
            p['x'] = p['home_x']
            p['y'] = p['home_y']
            p['vx'] = 0
            p['vy'] = 0
            
    if recording and frames_saved < 420:  # 420 = one full loop
        saveFrame("frames/frame-####.png")
        frames_saved += 1
        if frames_saved == 420:
            print("Recording complete! Check the frames folder.")
            recording = False
