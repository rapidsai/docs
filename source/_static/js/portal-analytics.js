// SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
// SPDX-License-Identifier: Apache-2.0

function OptanonWrapper() {
  window.dispatchEvent(new Event("bannerLoaded"));
}

function hasAnalyticsConsent() {
  return (
    typeof window.OnetrustActiveGroups === "string" &&
    window.OnetrustActiveGroups.split(",").includes("C0002")
  );
}

function loadGA4() {
  if (window._ga4Loaded) return;
  window._ga4Loaded = true;
  const gtagScript = document.createElement("script");
  gtagScript.async = true;
  gtagScript.src =
    "https://www.googletagmanager.com/gtag/js?id=G-DLJNCEWKZD";
  document.head.appendChild(gtagScript);
  window.dataLayer = window.dataLayer || [];
  window.gtag =
    window.gtag ||
    function gtag() {
      window.dataLayer.push(arguments);
    };
  window.gtag("js", new Date());
  window.gtag("config", "G-DLJNCEWKZD");
}

function initializeAnalytics() {
  if (hasAnalyticsConsent()) loadGA4();
  if (window._satellite && window._satellite.pageBottom) {
    window._satellite.pageBottom();
  }
}

window.addEventListener("load", initializeAnalytics);
if (window.OneTrust && typeof window.OneTrust.OnConsentChanged === "function") {
  window.OneTrust.OnConsentChanged(initializeAnalytics);
}
