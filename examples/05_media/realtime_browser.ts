/**
 * Minimal browser-side WebRTC setup for a realtime voice session.
 *
 * Security boundary: `ephemeralKey` must be minted by your backend. Never expose
 * a long-lived provider key in browser JavaScript. Consult the provider's current
 * realtime documentation before deployment because event names can evolve.
 */
export async function startRealtimeVoice(
  ephemeralKey: string,
  model: string,
): Promise<{ peer: RTCPeerConnection; events: RTCDataChannel }> {
  const peer = new RTCPeerConnection();
  const audio = document.createElement("audio");
  audio.autoplay = true;
  peer.ontrack = (event) => {
    audio.srcObject = event.streams[0] ?? null;
  };

  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  for (const track of stream.getTracks()) peer.addTrack(track, stream);

  const events = peer.createDataChannel("oai-events");
  events.addEventListener("open", () => {
    events.send(JSON.stringify({
      type: "session.update",
      session: {
        instructions: "Be concise, helpful, and disclose uncertainty.",
        turn_detection: { type: "server_vad" },
      },
    }));
  });

  const offer = await peer.createOffer();
  await peer.setLocalDescription(offer);

  const response = await fetch(
    `https://api.openai.com/v1/realtime?model=${encodeURIComponent(model)}`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${ephemeralKey}`,
        "Content-Type": "application/sdp",
      },
      body: offer.sdp,
    },
  );
  if (!response.ok) throw new Error(`Realtime handshake failed: ${response.status}`);

  await peer.setRemoteDescription({ type: "answer", sdp: await response.text() });
  return { peer, events };
}
