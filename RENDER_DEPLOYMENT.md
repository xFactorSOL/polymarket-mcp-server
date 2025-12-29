# 🚀 Render Deployment Guide

This guide will help you deploy the Polymarket MCP Server web dashboard to Render.

## Prerequisites

- A [Render](https://render.com) account
- Your Polymarket wallet credentials (optional - can run in DEMO mode)

## Quick Deploy

### Option 1: One-Click Deploy (Recommended)

1. Click the button below to deploy directly to Render:

   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

2. Connect your GitHub repository
3. Render will automatically detect the `render.yaml` file
4. Configure your environment variables (see below)
5. Deploy!

### Option 2: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Blueprint"
3. Connect your GitHub repository
4. Render will detect `render.yaml` and create the service
5. Configure environment variables
6. Deploy!

## Environment Variables

### Required for Full Trading Mode

If you want full trading capabilities, set these in the Render dashboard:

```env
POLYGON_PRIVATE_KEY=your_private_key_without_0x_prefix
POLYGON_ADDRESS=0xYourPolygonAddress
```

### Optional: DEMO Mode (Read-Only)

For read-only access without a wallet:

```env
DEMO_MODE=true
```

### Optional: API Credentials

These are auto-created if not provided, but you can set them manually:

```env
POLYMARKET_API_KEY=your_api_key
POLYMARKET_PASSPHRASE=your_passphrase
```

### Optional: Safety Limits

Customize these based on your risk tolerance:

```env
MAX_ORDER_SIZE_USD=1000.0
MAX_TOTAL_EXPOSURE_USD=5000.0
MAX_POSITION_SIZE_PER_MARKET=2000.0
MIN_LIQUIDITY_REQUIRED=10000.0
MAX_SPREAD_TOLERANCE=0.05
ENABLE_AUTONOMOUS_TRADING=true
REQUIRE_CONFIRMATION_ABOVE_USD=500.0
AUTO_CANCEL_ON_LARGE_SPREAD=true
```

### Optional: Chain Configuration

```env
POLYMARKET_CHAIN_ID=137  # 137 for mainnet, 80002 for Amoy testnet
LOG_LEVEL=INFO
```

## Configuration Steps

1. **After deployment starts**, go to your service settings
2. Navigate to "Environment" tab
3. Add the environment variables listed above
4. Click "Save Changes"
5. The service will automatically redeploy

## Accessing Your Dashboard

Once deployed, Render will provide a URL like:
```
https://polymarket-mcp-dashboard.onrender.com
```

The dashboard will be available at this URL.

## Features Available

### DEMO Mode (DEMO_MODE=true)
- ✅ Market discovery and search
- ✅ Real-time market analysis
- ✅ AI-powered insights
- ✅ Price monitoring
- ❌ Trading disabled (read-only)

### Full Mode (with wallet credentials)
- ✅ Everything in DEMO mode
- ✅ Place orders and execute trades
- ✅ Portfolio management
- ✅ Position tracking
- ✅ Real-time trade notifications

## Troubleshooting

### Service Won't Start

1. Check the logs in Render dashboard
2. Verify all required environment variables are set
3. Ensure `POLYGON_PRIVATE_KEY` doesn't have `0x` prefix
4. Check that `POLYGON_ADDRESS` starts with `0x`

### Dashboard Shows "Not Configured"

- This is normal if running in DEMO mode
- For full mode, ensure `POLYGON_PRIVATE_KEY` and `POLYGON_ADDRESS` are set
- Check logs for configuration errors

### Port Issues

- Render automatically sets the `PORT` environment variable
- The app is configured to use this automatically
- No manual port configuration needed

## Updating Your Deployment

1. Push changes to your GitHub repository
2. Render will automatically detect and redeploy
3. Or manually trigger a deploy from the Render dashboard

## Security Notes

⚠️ **Important Security Considerations:**

- Never commit your private keys to the repository
- Use Render's environment variables for all sensitive data
- Start with small amounts when testing trading features
- Review safety limits before enabling autonomous trading

## Support

For issues or questions:
- Check the [main README](README.md)
- Review [FAQ](FAQ.md)
- Open an issue on GitHub

## Cost

Render offers a free tier that should be sufficient for testing:
- 750 hours/month free
- Automatic SSL certificates
- Custom domains supported

For production use, consider upgrading to a paid plan for:
- Better performance
- No sleep on inactivity
- Priority support
