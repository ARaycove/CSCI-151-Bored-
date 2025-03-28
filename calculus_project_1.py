import numpy as np
import matplotlib.pyplot as plt

# Create time points (x-axis)
t = np.linspace(0, 240, 5000)  # Time from 0 to 240 seconds

def runner_a(t):
    # Runner A: Constant Pace Throughout Race
    b = (2*np.pi)/250
    distance = (2.68 * t) + 75*np.sin((b)*t)
    return distance
    
def runner_b(t):
    # Runner B: Starts fast but runner keeps speeding up and slowing down
    b = (2*np.pi)/50
    distance = 2.68*t + 10*np.sin(b*t)
    return distance
    
def runner_c(t):
    # Runner C: Very Fast start, but runner stops, then resumes
    distance = np.zeros_like(t)
    b = (2*np.pi)/300
    # Create masks for different time segments
    mask1 = t <= 10
    mask2 = (t > 10) & (t < 30)
    mask3 = t >= 30
    
    # Apply calculations with continuity adjustments
    distance[mask1] = 4.917 * t[mask1]
    
    # At t=10, the value is 4.917*10 = 49.17
    distance[mask2] = 4.917 * 10  # Constant value during rest
    
    # At t=20, we need to match the value 49.17
    # 2.7*20 = 54, so we need an offset of 49.17-54 = -4.83
    adjustment = 49.17 - ((2.72 * 30)+60*np.sin(b*t[mask3][0]))
    distance[mask3] = 2.72 * t[mask3] + adjustment + 60*np.sin(b*t[mask3])
    return distance

# Find crossings (lead changes)
def find_crossings(t, dist1, dist2, runner1, runner2):
    for i in range(1, len(t)):
        if (dist1[i-1] - dist2[i-1]) * (dist1[i] - dist2[i]) <= 0:  # Sign change indicates crossing
            # Interpolate to find more precise crossing time
            t_cross = t[i-1] + (t[i] - t[i-1]) * abs((dist1[i-1] - dist2[i-1]) / 
                                                   (dist1[i] - dist2[i] - dist1[i-1] + dist2[i-1]))
            
            # Only report if it's an actual crossing, not just touching
            if abs(dist1[i] - dist2[i]) > 1e-10:
                print(f"Lead change at t ≈ {t_cross:.2f} seconds: {runner1} and {runner2} cross")

def distance_between_runners(time):
    # If time is a scalar, convert to a single-element array for the runner functions
    if np.isscalar(time):
        t_array = np.array([time])
        dist_a_at_t = runner_a(t_array)[0]  # Extract scalar result
        dist_b_at_t = runner_b(t_array)[0]
        dist_c_at_t = runner_c(t_array)[0]
    else:
        # If already an array, use as is
        dist_a_at_t = runner_a(time)
        dist_b_at_t = runner_b(time)
        dist_c_at_t = runner_c(time)
    
    # Calculate distances between runners
    dist_a_b = abs(dist_a_at_t - dist_b_at_t)
    dist_a_c = abs(dist_a_at_t - dist_c_at_t)
    dist_b_c = abs(dist_b_at_t - dist_c_at_t)
    
    return {
        'A-B': dist_a_b, 
        'A-C': dist_a_c, 
        'B-C': dist_b_c
    }

def get_derivative(input_arrays, t_range=t):
    # Calculate time step for differentiation
    dt = t_range[1] - t_range[0]
    
    # Calculate derivatives using np.gradient
    derivatives = []
    for arr in input_arrays:
        derivatives.append(np.gradient(arr, dt))
    
    # Find max and min values with their corresponding times
    result = {}
    for i, deriv in enumerate(derivatives):
        label = f"Array {i+1}"
        result[label] = {
            'max_value': np.max(deriv),
            'max_time': t_range[np.argmax(deriv)],
            'min_value': np.min(deriv),
            'min_time': t_range[np.argmin(deriv)]
        }
    
    # Return result dictionary and individual derivatives
    return result, *derivatives

# Run equations and map into array
dist_a = runner_a(t)
dist_b = runner_b(t)
dist_c = runner_c(t)
#####################
# Get Derivatives velocity and acceleration
velocity_data,      v_a, v_b, v_c   = get_derivative([dist_a, dist_b, dist_c])
acceleration_data,  a_a, a_b, a_c   = get_derivative([v_a, v_b, v_c])
# Check all pairs of runners for crossings
find_crossings(t, dist_a, dist_b, "Runner A", "Runner B")
find_crossings(t, dist_a, dist_c, "Runner A", "Runner C")
find_crossings(t, dist_b, dist_c, "Runner B", "Runner C")

# Create the plots in one figure with two subplots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 15))
# Plot 1: Distance vs Time
ax1.plot(t, dist_a, 'k-', linewidth=2, label='Runner A')
ax1.plot(t, dist_b, 'k--', linewidth=2, label='Runner B')
ax1.plot(t, dist_c, 'k:', linewidth=2, label='Runner C')
ax1.grid(True)
ax1.set_xticks(np.arange(0, 241, 10))
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Distance (meters)')
ax1.set_title('Race Progress: Distance vs Time')
ax1.legend()
ax1.set_xlim(0, 240)
ax1.set_ylim(0, 500)

# Plot 2: Velocity (derivative) vs Time
ax2.plot(t, v_a, 'k-', linewidth=2, label='Runner A')
ax2.plot(t, v_b, 'k--', linewidth=2, label='Runner B')
ax2.plot(t, v_c, 'k:', linewidth=2, label='Runner C')
ax2.grid(True)
ax2.set_xticks(np.arange(0, 241, 10))
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Velocity (m/s)')
ax2.set_title('Runner Velocities')
ax2.legend()
ax2.set_xlim(0, 240)

# Plot 3: acceleration (derivative) vs Time
ax3.plot(t, a_a, 'k-', linewidth=2, label='Runner A')
ax3.plot(t, a_b, 'k--', linewidth=2, label='Runner B')
ax3.grid(True)
ax3.set_xticks(np.arange(0, 241, 10))
ax3.set_xlabel('Time (seconds)')
ax3.set_ylabel('Acceleration (m/s)')
ax3.set_title('Runner Acceleration')
ax3.legend()
ax3.set_xlim(0, 240)

# Plot 4: acceleration vs Time, Just Runner C
ax4.plot(t, a_c, 'k:', linewidth=2, label='Runner C')
ax4.grid(True)
ax4.set_xticks(np.arange(0, 241, 10))
ax4.set_xlabel('Time (seconds)')
ax4.set_ylabel('Acceleration (m/s)')
ax4.set_title('Runner Acceleration')
ax4.legend()
ax4.set_xlim(0, 240)
ax4.set_ylim(-1, 1)

# Adjust spacing between subplots
plt.tight_layout()
# Save and show the figure
plt.savefig("graph.png")

'''
1.
a) Time and distance scales are imposed on a gridded plane
b) 5 lead changes are present in the graph
c) A variety of velocities among the three runners exist, including a 0 period
d) There are intervals of negative and positive acceleration in the graphs
2.
a) The Race was ended at exactly 230.63 seconds, when person C crossed the finish line
b) 
- At time 10 seconds, Runner C fell down trying to keep up with Runner A
- At time 10.83, Runner A passed Runner C after he fell
- At time 14.77, Runner B passes Runner C
- Runner contemplates his life for a while
- At time 30, Runner C resumes the race
- At time 78.96 Runner C passes Runner B
- At time 92.57 Runner B passes Runner C as he runs out of energy
- At time 125 Runner B passes Runner A
- At time 190.10 Runner B finishes
- At time 210.14 Runner A finishes
- At time 230.63 Runner C finishes
c) The runners were closest together around the 10-12 second mark
d) The Greatest Lead was for Runner A at time 80 seconds, he was approximately 73.46m from Runner B and 98.36m from Runner C

3. I can run a second function that uses the derivative operator to find the point at which each one ran the fastest
a) 
Runner A:
  Max velocity: 4.56 m/s at t=0.00s
  Min velocity: 0.80 m/s at t=124.92s
Runner B:
  Max velocity: 3.94 m/s at t=0.00s
  Min velocity: 1.42 m/s at t=24.98s
Runner C:
  Max velocity: 4.92 m/s at t=6.25s
  Min velocity: 0.00 m/s at t=10.33s
b) Every runners velocity varied over the course of the race,
The graph of the derivative is also recorded.
c) Three "interesting" times
- When the Runner C falls, velocity drops to 0,
- When Runner C briefly passes Runner B, velocity of runner c is slowing and crosses the graph of Runner B's velocity
- Runner A has a very large lead @ time 80, Runner A's velocity is its lowest acceleration (the transition between concave down and concave up)
d) 
Runner B is a pure sinusoidal graph, velocity fluctuates consistently
Runner A is also a cos graph, but with a larger range of velocities

4. I can use Python to generate the graph of acceleration now as well
a) 
Runner A has a positive/negative acceleration over intervals: 125 seconds
- negative 0 - 125
- positive 125 - end of race
- Zero at every 125 second interval, at that exact point in time
Runner B has a positive/negative acceleration over intervals: 25 seconds
- negative 0-25,50-75,100-125, etc.
- positive 25-50, 75-100, 125-150, etc.
- zero at interval k*25
Runner C has two extreme spikes at 10 seconds, and 35 seconds
- zero from 0-10 seconds (starts at steady rate)
- negative acceleration of -45 @ 10 seconds,
- zero from 10 to 35
- positive 35 @ 35 seconds
- negative from 35 to 140 seconds
- zero @ 140 seconds
- positive till end of race
b) Important moments
- The runner C abruptly stops, resulting in a massive deceleration spike in the graph
- All other shifts to negative acceleration follows the same sin wave, steady increase and decrease
c) Choose three “interesting” times in the race and describe the runners' accelerations at these times.
- When runner C falls, acceleration is very large (~-45m/s)
- When runner C starts off running again acceleration is very large (~30m/s)
- Only for that brief moment in time, then acceleration does not change much at all
- When Runner B pass Runner A
    - Runner A has been decelerating for a long time, but Runner B is also decelerating at that point in time. 
- When Runner C passes Runner B
    - Runner C is in the middle of their deceleration interval
    - Runner B is at the peak of their acceleration interval
    - Indicating that B at this time is still speeding back up (near lower end of velocity)
    - And Runner C is still nearer to the their max velocity
d) Any other acceleration-related information that you can extract from the graph?
- No not really, but plotting does confirm the derivative of a sinusoidal graph is a differrent sinusoidal graph.

5. Time Stamped Commentary
000 Seconds: And they're off! The runners explode from the starting line on this beautiful day!

005 Seconds: What a start we're seeing! Runner A and C are neck and neck

010 Seconds: Oh no! Something's happened to Runner C! They've pulled up suddenly - looks like they might be cramping. This could be devastating for their chances.

015 Seconds: Runner A continues to power ahead while B has settled into a steady rhythm. C is still not moving - this doesn't look good, folks.

025 Seconds: Runner A building a commanding lead now. B seems to be using an interesting strategy - speeding up and slowing down. Meanwhile, the medical team is with Runner C.

030 Seconds: Wait a minute! Runner C is moving again! They're back in the race after that brief stoppage! The crowd is going wild!

045 Seconds: Runner A still leading the pack, but B is starting to make a move. And would you look at C - making up ground after that early setback!

080 Seconds: Looks like Runner C just passed Runner B, He's still in it folks!
090 Seconds: Well that was short lived, Guess he's running out of steam

110 Seconds: The gap is closing! Runner B is really making up ground on our leader. Runner A seems to be hitting a bit of a wall at this point.

125 Seconds: B has done it! We have a new leader! What a turnaround in this race! Runner A led for so long but B has taken control now!

150 Seconds: Runner B continuing to pull away. A is trying to respond but doesn't seem to have an answer right now. And C is still battling away - what heart after that early mishap!

170 Seconds: As we approach the finish, B has a comfortable lead. But look at Runner A - finding something extra, picking up the pace in these closing stages!

190 Seconds: Runner B crosses the line first! What a performance with that unique pacing strategy paying dividends in the end!

210 Seconds: And here comes Runner A for second place! Led for over half the race but couldn't hold off B's charge.

230 Seconds: Completing our field is Runner C! What a story of perseverance - stopped early on but refused to give up. That's the spirit of competition right there, ladies and gentlemen!

'''