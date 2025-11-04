import React, { useEffect, useState } from 'react';
import { useSpring, animated } from 'react-spring';
import './Particles.css';

interface ParticleProps {
  delay: number;
  color: string;
}

interface ParticleData {
  id: number;
  delay: number;
  color: string;
}

function Particle({ delay, color }: ParticleProps) {
  const props = useSpring({
    from: {
      opacity: 1,
      transform: 'translate(0px, 0px) scale(1)',
    },
    to: async (next) => {
      await next({
        opacity: 0,
        transform: `translate(${Math.random() * 200 - 100}px, ${-Math.random() * 200 - 50}px) scale(0)`,
      });
    },
    config: { duration: 1000 },
    delay,
  });

  return (
    <animated.div
      className="particle"
      style={{
        ...props,
        background: color,
      }}
    />
  );
}

function Particles() {
  const [particles, setParticles] = useState<ParticleData[]>([]);
  const colors = ['#ff006e', '#8338ec', '#3a86ff', '#00ff00', '#ffbe0b'];

  useEffect(() => {
    // Generate 30 particles with random colors and delays
    const newParticles = Array.from({ length: 30 }, (_, i) => ({
      id: i,
      delay: Math.random() * 300,
      color: colors[Math.floor(Math.random() * colors.length)],
    }));
    setParticles(newParticles);
  }, []);

  return (
    <div className="particles-container">
      {particles.map((particle) => (
        <Particle
          key={particle.id}
          delay={particle.delay}
          color={particle.color}
        />
      ))}
    </div>
  );
}

export default Particles;
