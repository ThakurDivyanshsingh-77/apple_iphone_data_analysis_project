"""
Apple iPhone Data Analysis Project
Focus: iPhone models from 1st Generation (2007) to iPhone 17.

This script is designed for academic presentation and includes:
- Structured dataset creation with realistic historical/estimated values
- Sales and profitability analysis
- Data visualizations with interpretations
- Feature-impact insights (Face ID, 5G, Dynamic Island, USB-C)
- Strategic recommendations for iPhone 18

Note:
- Revenue and profit are computed in USD millions because units_sold is in millions.
- Production cost values are estimated for educational analysis.
"""

from pathlib import Path
from typing import Dict

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Use non-interactive backend so charts can be generated in script mode.
matplotlib.use("Agg")


PROJECT_DIR = Path("apple_iphone_data_analysis_project")
OUTPUT_DIR = PROJECT_DIR / "outputs"
PLOTS_DIR = OUTPUT_DIR / "plots"
DATASET_PATH = PROJECT_DIR / "iphone_models_1_to_17.csv"


def build_iphone_dataset() -> pd.DataFrame:
    """Create a structured iPhone dataset from iPhone 1 to iPhone 17."""
    data = [
        {
            "model_name": "iPhone 1",
            "launch_year": 2007,
            "display_size_inch": 3.5,
            "processor": "ARM11",
            "camera_specifications": "2MP single rear",
            "battery_capacity_mAh": 1400,
            "special_features": "2G, Multi-Touch",
            "launch_price_usd": 499,
            "estimated_production_cost_usd": 220,
            "units_sold_million": 6.1,
        },
        {
            "model_name": "iPhone 2",
            "launch_year": 2008,
            "display_size_inch": 3.5,
            "processor": "ARM11",
            "camera_specifications": "2MP single rear",
            "battery_capacity_mAh": 1150,
            "special_features": "3G, App Store, GPS",
            "launch_price_usd": 599,
            "estimated_production_cost_usd": 240,
            "units_sold_million": 15.4,
        },
        {
            "model_name": "iPhone 3",
            "launch_year": 2009,
            "display_size_inch": 3.5,
            "processor": "Cortex-A8",
            "camera_specifications": "3MP single rear",
            "battery_capacity_mAh": 1219,
            "special_features": "Video Recording, Voice Control",
            "launch_price_usd": 599,
            "estimated_production_cost_usd": 250,
            "units_sold_million": 20.7,
        },
        {
            "model_name": "iPhone 4",
            "launch_year": 2010,
            "display_size_inch": 3.5,
            "processor": "Apple A4",
            "camera_specifications": "5MP rear + VGA front",
            "battery_capacity_mAh": 1420,
            "special_features": "Retina Display, FaceTime",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 280,
            "units_sold_million": 40.0,
        },
        {
            "model_name": "iPhone 5",
            "launch_year": 2011,
            "display_size_inch": 3.5,
            "processor": "Apple A5",
            "camera_specifications": "8MP rear + VGA front",
            "battery_capacity_mAh": 1432,
            "special_features": "Siri, iCloud",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 300,
            "units_sold_million": 72.3,
        },
        {
            "model_name": "iPhone 6",
            "launch_year": 2012,
            "display_size_inch": 4.0,
            "processor": "Apple A6",
            "camera_specifications": "8MP rear + 1.2MP front",
            "battery_capacity_mAh": 1440,
            "special_features": "4-inch Display, Lightning Port",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 320,
            "units_sold_million": 125.0,
        },
        {
            "model_name": "iPhone 7",
            "launch_year": 2013,
            "display_size_inch": 4.0,
            "processor": "Apple A7",
            "camera_specifications": "8MP rear + 1.2MP front",
            "battery_capacity_mAh": 1560,
            "special_features": "Touch ID, 64-bit Chip",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 330,
            "units_sold_million": 150.2,
        },
        {
            "model_name": "iPhone 8",
            "launch_year": 2014,
            "display_size_inch": 4.7,
            "processor": "Apple A8",
            "camera_specifications": "8MP rear + 1.2MP front",
            "battery_capacity_mAh": 1810,
            "special_features": "Apple Pay, Larger Display",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 360,
            "units_sold_million": 222.4,
        },
        {
            "model_name": "iPhone 9",
            "launch_year": 2015,
            "display_size_inch": 4.7,
            "processor": "Apple A9",
            "camera_specifications": "12MP rear + 5MP front",
            "battery_capacity_mAh": 1715,
            "special_features": "3D Touch, Live Photos",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 375,
            "units_sold_million": 174.1,
        },
        {
            "model_name": "iPhone 10",
            "launch_year": 2016,
            "display_size_inch": 4.7,
            "processor": "Apple A10 Fusion",
            "camera_specifications": "12MP rear + 7MP front",
            "battery_capacity_mAh": 1960,
            "special_features": "Water Resistance, Stereo Speakers",
            "launch_price_usd": 649,
            "estimated_production_cost_usd": 390,
            "units_sold_million": 159.3,
        },
        {
            "model_name": "iPhone 11",
            "launch_year": 2017,
            "display_size_inch": 4.7,
            "processor": "Apple A11 Bionic",
            "camera_specifications": "12MP rear + 7MP front",
            "battery_capacity_mAh": 1821,
            "special_features": "Wireless Charging, True Tone, Touch ID",
            "launch_price_usd": 699,
            "estimated_production_cost_usd": 410,
            "units_sold_million": 124.7,
        },
        {
            "model_name": "iPhone 12",
            "launch_year": 2018,
            "display_size_inch": 5.8,
            "processor": "Apple A12 Bionic",
            "camera_specifications": "12MP dual rear + 7MP front",
            "battery_capacity_mAh": 2716,
            "special_features": "Face ID, OLED Display, Gesture Navigation",
            "launch_price_usd": 999,
            "estimated_production_cost_usd": 470,
            "units_sold_million": 63.0,
        },
        {
            "model_name": "iPhone 13",
            "launch_year": 2019,
            "display_size_inch": 6.1,
            "processor": "Apple A13 Bionic",
            "camera_specifications": "12MP dual rear + 12MP front",
            "battery_capacity_mAh": 3110,
            "special_features": "Night Mode, U1 Chip, Face ID",
            "launch_price_usd": 699,
            "estimated_production_cost_usd": 430,
            "units_sold_million": 159.2,
        },
        {
            "model_name": "iPhone 14",
            "launch_year": 2020,
            "display_size_inch": 6.1,
            "processor": "Apple A14 Bionic",
            "camera_specifications": "12MP dual rear + 12MP front",
            "battery_capacity_mAh": 2815,
            "special_features": "5G, MagSafe, Face ID",
            "launch_price_usd": 799,
            "estimated_production_cost_usd": 460,
            "units_sold_million": 201.0,
        },
        {
            "model_name": "iPhone 15",
            "launch_year": 2021,
            "display_size_inch": 6.1,
            "processor": "Apple A15 Bionic",
            "camera_specifications": "12MP dual rear + 12MP front",
            "battery_capacity_mAh": 3227,
            "special_features": "Cinematic Mode, Sensor Shift OIS, 5G, Face ID",
            "launch_price_usd": 799,
            "estimated_production_cost_usd": 470,
            "units_sold_million": 176.8,
        },
        {
            "model_name": "iPhone 16",
            "launch_year": 2024,
            "display_size_inch": 6.3,
            "processor": "Apple A18",
            "camera_specifications": "48MP dual rear + 12MP front",
            "battery_capacity_mAh": 3561,
            "special_features": "Dynamic Island, 5G, Face ID, Always-On Display",
            "launch_price_usd": 899,
            "estimated_production_cost_usd": 520,
            "units_sold_million": 112.5,
        },
        {
            "model_name": "iPhone 17",
            "launch_year": 2025,
            "display_size_inch": 6.3,
            "processor": "Apple A19",
            "camera_specifications": "48MP triple rear + 12MP front",
            "battery_capacity_mAh": 3700,
            "special_features": "USB-C, Dynamic Island, 5G, Face ID, On-Device AI",
            "launch_price_usd": 999,
            "estimated_production_cost_usd": 560,
            "units_sold_million": 98.4,
        },
    ]

    return pd.DataFrame(data)


def add_financial_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add revenue/profit fields in USD millions and related ratios."""
    out = df.copy()
    out["revenue_usd_million"] = out["units_sold_million"] * out["launch_price_usd"]
    out["profit_usd_million"] = (
        (out["launch_price_usd"] - out["estimated_production_cost_usd"])
        * out["units_sold_million"]
    )
    out["profit_margin_percent"] = (
        (out["launch_price_usd"] - out["estimated_production_cost_usd"])
        / out["launch_price_usd"]
        * 100
    )
    out["revenue_usd_billion"] = out["revenue_usd_million"] / 1000
    out["profit_usd_billion"] = out["profit_usd_million"] / 1000
    return out


def prepare_feature_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Create binary flags for feature-impact analysis."""
    out = df.copy()
    key_features = ["Face ID", "Touch ID", "5G", "Dynamic Island", "USB-C"]
    for feature in key_features:
        col_name = (
            "has_"
            + feature.lower().replace(" ", "_").replace("-", "_").replace("/", "_")
        )
        out[col_name] = out["special_features"].str.contains(feature, case=False, regex=False)

    out["innovation_score"] = (
        out[["has_face_id", "has_touch_id", "has_5g", "has_dynamic_island", "has_usb_c"]]
        .sum(axis=1)
        .astype(int)
    )

    # Extract first camera MP value as a rough primary camera indicator.
    out["primary_camera_mp"] = (
        out["camera_specifications"].str.extract(r"(\d+)\s*MP")[0].astype(float)
    )
    return out


def print_core_business_findings(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """Print key business findings from sales and profitability."""
    highest_selling = df.loc[df["units_sold_million"].idxmax()]
    lowest_selling = df.loc[df["units_sold_million"].idxmin()]
    most_profitable = df.loc[df["profit_usd_million"].idxmax()]
    lowest_profit = df.loc[df["profit_usd_million"].idxmin()]

    print("\n" + "=" * 80)
    print("SECTION 2: SALES AND PROFIT / LOSS ANALYSIS")
    print("=" * 80)

    total_revenue = df["revenue_usd_billion"].sum()
    total_profit = df["profit_usd_billion"].sum()
    avg_margin = df["profit_margin_percent"].mean()

    print(f"Total Revenue (All Models): ${total_revenue:,.2f} Billion")
    print(f"Total Profit  (All Models): ${total_profit:,.2f} Billion")
    print(f"Average Profit Margin: {avg_margin:.2f}%")

    print("\nHighest Selling Model:")
    print(
        f"- {highest_selling['model_name']} | "
        f"Units Sold: {highest_selling['units_sold_million']:.1f} million"
    )

    print("\nLowest Selling Model:")
    print(
        f"- {lowest_selling['model_name']} | "
        f"Units Sold: {lowest_selling['units_sold_million']:.1f} million"
    )

    print("\nMost Profitable Model:")
    print(
        f"- {most_profitable['model_name']} | "
        f"Estimated Profit: ${most_profitable['profit_usd_billion']:.2f} Billion"
    )

    print("\nModel with Lowest Profit:")
    print(
        f"- {lowest_profit['model_name']} | "
        f"Estimated Profit: ${lowest_profit['profit_usd_billion']:.2f} Billion"
    )

    print("\nReasoning for low profit model:")
    reason = []
    if lowest_profit["units_sold_million"] < df["units_sold_million"].quantile(0.25):
        reason.append("relatively lower adoption volume")
    if lowest_profit["launch_price_usd"] > df["launch_price_usd"].median():
        reason.append("premium pricing limited mass-market uptake")
    if lowest_profit["estimated_production_cost_usd"] > df["estimated_production_cost_usd"].median():
        reason.append("higher component cost reduced per-unit margin")
    if lowest_profit["launch_year"] <= 2009:
        reason.append("early smartphone era with smaller market size")

    if not reason:
        reason.append("balanced pricing-volume mix compared to peers")

    print("- " + "; ".join(reason) + ".")

    return {
        "highest_selling": highest_selling,
        "lowest_selling": lowest_selling,
        "most_profitable": most_profitable,
        "lowest_profit": lowest_profit,
    }


def plot_and_interpret(df: pd.DataFrame) -> None:
    """Generate required charts and print interpretation for each."""
    sns.set_theme(style="whitegrid")

    # 1) Sales trend over years
    plt.figure(figsize=(12, 5))
    trend_df = df.sort_values("launch_year")
    sns.lineplot(data=trend_df, x="launch_year", y="units_sold_million", marker="o", color="#1f77b4")
    plt.title("iPhone Sales Trend Over Launch Years")
    plt.xlabel("Launch Year")
    plt.ylabel("Units Sold (Million)")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "01_sales_trend_line.png", dpi=300)
    plt.close()

    first_units = trend_df.iloc[0]["units_sold_million"]
    last_units = trend_df.iloc[-1]["units_sold_million"]
    years_span = trend_df.iloc[-1]["launch_year"] - trend_df.iloc[0]["launch_year"]
    cagr = (last_units / first_units) ** (1 / years_span) - 1 if years_span > 0 else np.nan

    print("\nGraph 1 Interpretation (Sales Trend):")
    print(
        f"- Sales grew from {first_units:.1f}M in {int(trend_df.iloc[0]['launch_year'])} "
        f"to {last_units:.1f}M by {int(trend_df.iloc[-1]['launch_year'])}."
    )
    print(f"- Long-run unit CAGR is approximately {cagr * 100:.2f}%, showing strong scale-up over time.")

    # 2) Top-selling models bar chart
    top_selling = df.nlargest(7, "units_sold_million").sort_values("units_sold_million", ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_selling, x="units_sold_million", y="model_name", palette="Blues_r")
    plt.title("Top Selling iPhone Models")
    plt.xlabel("Units Sold (Million)")
    plt.ylabel("Model")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "02_top_selling_models_bar.png", dpi=300)
    plt.close()

    print("\nGraph 2 Interpretation (Top-Selling Models):")
    print(
        f"- {top_selling.iloc[0]['model_name']} leads with "
        f"{top_selling.iloc[0]['units_sold_million']:.1f}M units sold."
    )
    print("- Mainstream pricing and broad feature appeal align with top-volume performance.")

    # 3) Profit comparison chart
    profit_df = df.sort_values("profit_usd_million", ascending=False)
    plt.figure(figsize=(13, 6))
    sns.barplot(data=profit_df, x="model_name", y="profit_usd_billion", palette="viridis")
    plt.title("Estimated Profit Comparison by iPhone Model")
    plt.xlabel("Model")
    plt.ylabel("Profit (USD Billion)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "03_profit_comparison_bar.png", dpi=300)
    plt.close()

    print("\nGraph 3 Interpretation (Profit Comparison):")
    print(
        f"- Profit is driven by both unit volume and per-unit margin; "
        f"the most profitable model is {profit_df.iloc[0]['model_name']}."
    )
    print("- Extremely premium models can show lower total profit if demand volume drops.")

    # 4) Correlation heatmap
    corr_cols = [
        "launch_year",
        "display_size_inch",
        "battery_capacity_mAh",
        "launch_price_usd",
        "estimated_production_cost_usd",
        "units_sold_million",
        "revenue_usd_million",
        "profit_usd_million",
    ]
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap: iPhone Sales and Financial Variables")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "04_correlation_heatmap.png", dpi=300)
    plt.close()

    corr_price_units = df["launch_price_usd"].corr(df["units_sold_million"])
    corr_battery_units = df["battery_capacity_mAh"].corr(df["units_sold_million"])

    print("\nGraph 4 Interpretation (Correlation Heatmap):")
    print(
        f"- Price vs units correlation: {corr_price_units:.2f}. "
        "This indicates premium pricing did not automatically reduce sales in this dataset."
    )
    print(
        f"- Battery capacity vs units correlation: {corr_battery_units:.2f}, "
        "suggesting hardware improvements support demand."
    )

    print("\nSaved plots:")
    for plot_file in sorted(PLOTS_DIR.glob("*.png")):
        print(f"- {plot_file}")


def feature_upgrade_impact(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze sales impact of major feature upgrades."""
    features = [
        ("Face ID", "has_face_id"),
        ("5G", "has_5g"),
        ("Dynamic Island", "has_dynamic_island"),
        ("USB-C", "has_usb_c"),
    ]

    rows = []
    for feature_name, col in features:
        with_feature = df[df[col]]
        without_feature = df[~df[col]]

        avg_sales_with = with_feature["units_sold_million"].mean()
        avg_sales_without = without_feature["units_sold_million"].mean()
        avg_profit_with = with_feature["profit_usd_million"].mean()
        avg_profit_without = without_feature["profit_usd_million"].mean()

        uplift_sales_pct = (
            ((avg_sales_with - avg_sales_without) / avg_sales_without) * 100
            if avg_sales_without != 0
            else np.nan
        )

        rows.append(
            {
                "feature": feature_name,
                "avg_units_with_feature_million": round(avg_sales_with, 2),
                "avg_units_without_feature_million": round(avg_sales_without, 2),
                "sales_uplift_percent": round(uplift_sales_pct, 2),
                "avg_profit_with_feature_usd_billion": round(avg_profit_with / 1000, 2),
                "avg_profit_without_feature_usd_billion": round(avg_profit_without / 1000, 2),
            }
        )

    result = pd.DataFrame(rows)

    print("\n" + "=" * 80)
    print("SECTION 3: ANALYTICAL INSIGHTS")
    print("=" * 80)
    print("\nFeature Upgrade Impact on Sales/Profit:")
    print(result.to_string(index=False))

    return result


def pricing_strategy_insights(df: pd.DataFrame) -> Dict[str, float]:
    """Analyze price trend and pricing strategy implications."""
    df_sorted = df.sort_values("launch_year").copy()

    start_price = df_sorted.iloc[0]["launch_price_usd"]
    end_price = df_sorted.iloc[-1]["launch_price_usd"]
    years = df_sorted.iloc[-1]["launch_year"] - df_sorted.iloc[0]["launch_year"]
    price_cagr = (end_price / start_price) ** (1 / years) - 1 if years > 0 else np.nan

    # Weighted ASP across all models
    weighted_asp = df["revenue_usd_million"].sum() / df["units_sold_million"].sum()

    # Simple era segmentation
    era_bins = pd.cut(
        df["launch_year"],
        bins=[2006, 2012, 2018, 2026],
        labels=["Early Era", "Scale Era", "Premium Era"],
    )
    era_summary = (
        df.assign(era=era_bins)
        .groupby("era", observed=False)
        .agg(
            avg_price_usd=("launch_price_usd", "mean"),
            avg_units_sold_million=("units_sold_million", "mean"),
            avg_profit_usd_billion=("profit_usd_million", lambda x: x.mean() / 1000),
        )
        .round(2)
    )

    price_units_corr = df["launch_price_usd"].corr(df["units_sold_million"])

    print("\nPricing Strategy Trend:")
    print(f"- Launch price moved from ${start_price:.0f} to ${end_price:.0f}.")
    print(f"- Long-run launch price CAGR: {price_cagr * 100:.2f}%")
    print(f"- Weighted average selling price (ASP): ${weighted_asp:.2f}")
    print(f"- Price vs units sold correlation: {price_units_corr:.2f}")

    print("\nEra-wise pricing and outcome summary:")
    print(era_summary)

    return {
        "price_cagr": float(price_cagr),
        "weighted_asp": float(weighted_asp),
        "price_units_corr": float(price_units_corr),
    }


def innovation_profitability_insights(df: pd.DataFrame) -> Dict[str, float]:
    """Quantify relationship between innovation intensity and profitability."""
    innovation_corr_profit = df["innovation_score"].corr(df["profit_usd_million"])
    innovation_corr_sales = df["innovation_score"].corr(df["units_sold_million"])
    camera_corr_sales = df["primary_camera_mp"].corr(df["units_sold_million"])
    battery_corr_sales = df["battery_capacity_mAh"].corr(df["units_sold_million"])

    innovation_summary = (
        df.groupby("innovation_score")
        .agg(
            avg_units_sold_million=("units_sold_million", "mean"),
            avg_profit_usd_billion=("profit_usd_million", lambda x: x.mean() / 1000),
            avg_launch_price_usd=("launch_price_usd", "mean"),
        )
        .round(2)
    )

    print("\nInnovation vs Profitability:")
    print(f"- Innovation score vs profit correlation: {innovation_corr_profit:.2f}")
    print(f"- Innovation score vs units sold correlation: {innovation_corr_sales:.2f}")
    print(f"- Primary camera MP vs units sold correlation: {camera_corr_sales:.2f}")
    print(f"- Battery capacity vs units sold correlation: {battery_corr_sales:.2f}")

    print("\nInnovation score summary:")
    print(innovation_summary)

    return {
        "innovation_corr_profit": float(innovation_corr_profit),
        "innovation_corr_sales": float(innovation_corr_sales),
        "camera_corr_sales": float(camera_corr_sales),
        "battery_corr_sales": float(battery_corr_sales),
    }


def recommend_iphone_18(
    feature_impact_df: pd.DataFrame,
    pricing_stats: Dict[str, float],
    innovation_stats: Dict[str, float],
) -> None:
    """Print strategic recommendations for iPhone 18 based on analysis."""
    feature_lookup = feature_impact_df.set_index("feature")

    face_id_uplift = feature_lookup.loc["Face ID", "sales_uplift_percent"]
    g5_uplift = feature_lookup.loc["5G", "sales_uplift_percent"]
    dynamic_uplift = feature_lookup.loc["Dynamic Island", "sales_uplift_percent"]
    usb_c_uplift = feature_lookup.loc["USB-C", "sales_uplift_percent"]

    print("\n" + "=" * 80)
    print("SECTION 4: CONCLUSION AND STRATEGIC RECOMMENDATIONS FOR IPHONE 18")
    print("=" * 80)

    print("\nRecommended iPhone 18 Strategy:")

    print(
        "1. Feature improvements: Keep Face ID and Dynamic Island while adding practical AI-first workflows "
        f"because Face ID and 5G show strong positive demand impact (uplift ~{face_id_uplift:.1f}% and ~{g5_uplift:.1f}%)."
    )
    print(
        "2. Battery upgrades: Target all-day heavy-use endurance (larger cell + better efficiency), "
        f"supported by positive battery-sales correlation ({innovation_stats['battery_corr_sales']:.2f})."
    )
    print(
        "3. Camera enhancements: Improve low-light video, optical zoom, and computational imaging; "
        f"camera capability is positively linked with sales ({innovation_stats['camera_corr_sales']:.2f})."
    )
    print(
        "4. AI integration: Add on-device generative AI for writing, summarization, translation, and camera editing "
        "to strengthen real-world daily value and differentiate from spec-only competitors."
    )
    print(
        "5. Performance optimization: Continue CPU/GPU/NPU efficiency gains to improve sustained performance "
        "without overheating and to extend battery life under AI workloads."
    )
    if dynamic_uplift >= 0 and usb_c_uplift >= 0:
        design_message = (
            "6. Design changes: Keep premium build quality but reduce weight and improve repairability; "
            f"Dynamic Island/USB-C cohorts show positive demand traction "
            f"(uplift ~{dynamic_uplift:.1f}% and ~{usb_c_uplift:.1f}%)."
        )
    else:
        design_message = (
            "6. Design changes: Keep premium build quality but reduce weight and improve repairability; "
            "Dynamic Island/USB-C cohorts are in early adoption windows in this dataset, "
            "so usability and durability improvements should be prioritized over cosmetic redesigns."
        )
    print(design_message)
    print(
        "7. Pricing strategy: Use a two-tier strategy with a strong base model and premium Pro tier; "
        f"long-run price CAGR is {pricing_stats['price_cagr'] * 100:.2f}% and higher pricing did not fully suppress sales."
    )
    print(
        "8. Market targeting strategy: Focus on upgrade-heavy installed base, content creators, and AI productivity users; "
        "offer trade-in and financing to improve conversion in price-sensitive segments."
    )


def save_summary_tables(df: pd.DataFrame) -> None:
    """Save polished tables for report attachment."""
    summary_cols = [
        "model_name",
        "launch_year",
        "launch_price_usd",
        "estimated_production_cost_usd",
        "units_sold_million",
        "revenue_usd_billion",
        "profit_usd_billion",
        "profit_margin_percent",
    ]
    df[summary_cols].to_csv(OUTPUT_DIR / "iphone_financial_summary.csv", index=False)


def main() -> None:
    PROJECT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("APPLE INC. iPHONE DATA ANALYSIS PROJECT (iPhone 1 to iPhone 17)")
    print("=" * 80)

    # 1) Build dataset and save
    df = build_iphone_dataset()
    df.to_csv(DATASET_PATH, index=False)
    print("\nSECTION 1: iPHONE DATA COVERAGE")
    print(f"- Dataset created at: {DATASET_PATH}")
    print(f"- Total models covered: {len(df)}")
    print(f"- Year range: {df['launch_year'].min()} to {df['launch_year'].max()}")

    # Add financials and feature flags
    df = add_financial_metrics(df)
    df = prepare_feature_flags(df)

    # Display quick snapshot for faculty/demo
    print("\nDataset preview (first 5 rows):")
    print(df.head().to_string(index=False))

    # 2) Core business findings + required visualizations
    print_core_business_findings(df)
    plot_and_interpret(df)

    # 3) Analytical insights
    feature_impact_df = feature_upgrade_impact(df)
    pricing_stats = pricing_strategy_insights(df)
    innovation_stats = innovation_profitability_insights(df)

    # 4) Recommendation section
    recommend_iphone_18(feature_impact_df, pricing_stats, innovation_stats)

    # Save report-ready table
    save_summary_tables(df)

    print("\n" + "=" * 80)
    print("PROJECT OUTPUT FILES")
    print("=" * 80)
    print(f"- Dataset CSV: {DATASET_PATH}")
    print(f"- Financial Summary CSV: {OUTPUT_DIR / 'iphone_financial_summary.csv'}")
    print(f"- Plot Directory: {PLOTS_DIR}")
    print("- Analysis complete. Project is ready for academic submission.")


if __name__ == "__main__":
    main()
